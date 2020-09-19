"""
Server manages user data and requests.
User presses button to request a pose. Server calls response.py."""
from flask import Flask, jsonify, abort, request, url_for
from response import response
from get_position import getPositions 
import urllib, json
import requests
from flask_cors import CORS
import os

#########################################################################################################
# Posts/Requests
posts = [] # requested button
     # User requests a pose and it gets added to posts
app = Flask(__name__)
CORS(app)
@app.route("/posts", methods=["GET"]) 
def get_posts():
    return jsonify(posts), 201

@app.route("/posts", methods=["POST"])
def request_pose(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    post = {
        "position": request.json["position"],
        "mode": request.json["mode"],
        "vid_length": request.json["vid_length"]
    }
    stream = os.popen('ipconfig getifaddr en0') # gets ip address
    ip = stream.read().rstrip() # gets rid of newline
    url_settings = "http://" + ip + ":61405/pixelsettings"
    settings = requests.get(url_settings)
    settings = settings.json()[-1]
    response(post) # action
    posts.append(post) # see post on website
    return jsonify(posts), 201
    # Run this to add a post
    # curl -i -H "Content-Type: application/json" -X POST -d '{"position":"0", "mode":"hi", "vid_length":"hi"}' http://192.168.1.8:61405/posts

#########################################################################################################
# Add and delete buttons
buttons = []

@app.route("/buttons", methods=["GET"]) 
def get_buttons():
    with open("user_data/buttons.json", "r+") as file:
        buttons = json.load(file)
    return jsonify(buttons), 201

@app.route("/buttons", methods=["POST"])
def add_button(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    with open("user_data/buttons.json", "r+") as file:
        data = json.load(file)
        button = {
        "id": request.json["id"],
        "title": request.json["title"],
        "position": request.json["position"],
        "mode": request.json["mode"],
        "vid_length": request.json["vid_length"]
    }
        data.append(button)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return jsonify(data), 201

@app.route("/buttons/<id>", methods=["DELETE"]) 
def delete_buttons(id):
    with open("user_data/buttons.json", "r+") as file:
        data = json.load(file)
        cnt = 0
        for button in data:
            if button["id"] == id:
                break
            cnt += 1
        del data[cnt]
        file.seek(0) # reset the file pointer to position 0 
        json.dump(data, file, indent=4) # overwrite file with dict
        file.truncate() # delete everything after the list
    return jsonify(data), 201
# curl -X DELETE "http://192.168.1.8:61405/buttons/bf1f6b44-8716-4a1e-88bc-7d830478fcb0"

#########################################################################################################
# Get pixels, not ready for parsing
pixel_settings = []
cmd_computer = "system_profiler SPHardwareDataType | grep  \'Model Identifier\'" 
# get model identifier of computer
# system_profiler SPHardwareDataType | grep "Model Identifier"
stream_computer = os.popen(cmd_computer)
computer = stream_computer.read().strip()[18:] # get rid of white space, remove Model Identifier
try:
    with open('user_data/' + computer + '.json', "r+") as file:
        pixel_settings = json.load(file) 
    with open('user_data/pixel_settings.json', "w") as file: # write to pixel_settings
        json.dump(pixel_settings, file, indent=4)
except OSError:
    with open("user_data/pixel_settings.json", "r+") as file:
        pixel_settings = json.load(file)

@app.route("/pixelsettings", methods=["GET"]) 
def get_pixel_settings():
    with open("user_data/pixel_settings.json", "r+") as file:
        pixel_settings = json.load(file)
    return jsonify(pixel_settings), 201

@app.route("/pixelsettings", methods=["POST"])
def edit_setting(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    setting = {
        "id": request.json["id"],
        "x": request.json["x"],
        "y": request.json["y"],
    }
    with open("user_data/pixel_settings.json", "r+") as file:
        data = json.load(file)
        cnt = 0
        for obj in data:
            if obj["id"] == setting["id"]:
                break
            cnt += 1 # indice of object in data
        data[cnt]["x"] = setting["x"]
        data[cnt]["y"] = setting["y"]
        file.seek(0)  # rewind
        json.dump(data, file, indent=4)
        file.truncate()
    return jsonify(data), 201

@app.route("/getpositions", methods=["POST"])
def get_pixels(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    setting = {
        "name": request.json["name"],
    }
    get_pixels = getPositions()
    x, y = get_pixels.mouse_listen()
    with open("user_data/pixel_settings.json", "r+") as file:
        data = json.load(file)
        cnt = 0
        for obj in data:
            if obj["name"] == setting["name"]:
                break
            cnt += 1 # indice of object in data
        data[cnt]["x"] = x
        data[cnt]["y"] = y
        file.seek(0)  # rewind
        json.dump(data, file, indent=4)
        file.truncate()
    return jsonify(data), 201

if __name__ == "__main__":
    stream = os.popen('ipconfig getifaddr en0')
    ip = stream.read().rstrip() # get ip address
    # don't generate qr bc http website can't scan it
    # os.system("python3 generate_qr.py &") # & let's local_server.py and generate_qr.py run at the same time
    # app.run(host=ip, port=61405, debug=True, use_reloader=False)
    # app.run(host=ip, port=61405, debug=True)
    app.run(host=ip, port=61405)
    # set use_reloader to false so the python script runs only once
    # reloader reloads the page each time i save an edit
    
    

