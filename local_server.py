"""
Server manages user data and requests.
User presses button to request a pose. Server calls response.py."""
from flask import Flask, jsonify, abort, request, url_for
from response import response 
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
    stream = os.popen('ipconfig getifaddr en0') # gets ip address: 192.168.X.X
    ip = stream.read().rstrip() # gets rid of newline
    # url_settings = "http://" + ip + ":61405/settings"
    url_settings = "http://" + ip + ":61405/pixelsettings"
    settings = requests.get(url_settings)
    settings = settings.json()[-1]
    response(post) # action
    posts.append(post) # see post on website
    return jsonify(posts), 201
    # Run this to add a post
    # curl -i -H "Content-Type: application/json" -X POST -d '{"position":"click_arrow_to_right_stop_vid", "mode":"hi", "vid_length":"hi"}' http://192.168.1.8:61405/posts

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
  
if __name__ == "__main__":
    stream = os.popen('ipconfig getifaddr en0')
    ip = stream.read().rstrip() # get ip address
    app.run(host=ip, port=61405, debug=True) # how will local server know which host to run at?

