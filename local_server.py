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
    url_settings = "http://" + ip + ":61405/settings"
    settings = requests.get(url_settings)
    settings = settings.json()[-1]
    response(post, settings) # action
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
    # data.append(button) # see post on website
    
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
# curl -i -H "Content-Type: application/json" -X DELETE -d '{"id":"a6c45aa5-25c2-470e-a6eb-2ccec9c35f2d"}' http://192.168.1.8:61405/buttons/<id>
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

#########################################################################################################
# Pixel Settings
"""DELETE JSON INSIDE SETTINGS WHEN DEPLOYING SERVICE"""
# settings = []
settings = [{
        "computer": "macbook pro 13-inch",
        "click_arrow_to_right_stop_vid": "170, 860",
        "click_vb_settings": "270, 780",
        "click_exit_settings": "345, 152",
        "click_reactions": "1039, 870",
        "click_thumbsup": "1058, 815",
        "click_clapping": "1020, 817",
        "0": "640, 571",
        "1": "765, 571",
        "2": "882, 571",
        "3": "1000, 571",
        "4": "640, 640",
        "5": "765, 640",
        "6": "882, 640",
        "7": "1000, 640",
        "8": "640, 715",
        "9": "765, 715",
        "10": "882, 715",
        "11": "1000, 715",
    }]

@app.route("/settings", methods=["GET"])
def get_settings(): # all settings on local server
    return jsonify(settings), 201

@app.route("/settings", methods=["POST"])
def initialize_settings():
    if not request.json:
        abort(400)
  
    setting = {
        "computer": request.json["computer"],
        "click_arrow_to_right_stop_vid": request.json["click_arrow_to_right_stop_vid"],
        "click_vb_settings": request.json["click_vb_settings"],
        "click_exit_settings": request.json["click_exit_settings"],
        "click_reactions": request.json["click_reactions"],
        "click_thumbsup": request.json["click_thumbsup"],
        "click_clapping": request.json["click_clapping"],
        "0": request.json["0"],
        "1": request.json["1"],
        "2": request.json["2"],
        "3": request.json["3"],
        "4": request.json["4"],
        "5": request.json["5"],
        "6": request.json["6"],
        "7": request.json["7"],
        "8": request.json["8"],
        "9": request.json["9"],
        "10": request.json["10"],
        "11": request.json["11"],
    }
    settings.append(setting)
    return jsonify(settings), 201
    # Run this to add settings for the user
    # curl -i -H "Content-Type: application/json" -X POST -d '{"os":"", "button_next_to_stop_vid":""}' http://192.168.1.8:61405/settings
    
if __name__ == "__main__":
    stream = os.popen('ipconfig getifaddr en0')
    ip = stream.read().rstrip()
    app.run(host=ip, port=61405, debug=True) # how will local server know which host to run at?

