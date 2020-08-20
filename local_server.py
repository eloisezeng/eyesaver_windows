"""
Server manages user data and requests.
User presses button to request a pose. Server calls response.py."""
from flask import Flask, jsonify, abort, request
from response import response 
import urllib, json
import requests

#########################################################################################################
# Posts/Requests

posts = [] # requested button
     # User requests a pose and it gets added to posts
app = Flask(__name__)

@app.route("/service/posts", methods=["GET"]) 
def get_posts():
    return jsonify(posts), 201

@app.route("/service/posts", methods=["POST"])
def request_pose(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    post = { # requested button
        "button": request.json["button"]
    }
    url_poses = "http://127.0.0.1:5000/service/poses"
    mapping = requests.get(url_poses)
    mapping = mapping.json()[-1] # get most recent request mapping for user
    url_settings = "http://127.0.0.1:5000/service/settings"
    settings = requests.get(url_settings)
    settings = settings.json()[-1]
    response(mapping, post["button"], settings) # action
    posts.append(post) # see post on website
    return jsonify(posts), 201

    # Run this to add a post
    # curl -i -H "Content-Type: application/json" -X POST -d '{"button":"7"}' http://127.0.0.1:5000/service/posts

#########################################################################################################
# Pose Mapping
"""DELETE JSON INSIDE POSES WHEN DEPLOYING SERVICE"""
"""Change to poses = []"""
poses = [{ 
        "thumbsup": "thumbsup",
        "clapping": "clapping",
        "0": "default", # no background
        "1": "default", # San Fran
        "2": "default", # Grass
        "3": "default", # Earth
        "4": "default", # Northern Lights
        "5": "default", # Beach
        "6": "default", # "default"
        "7": "distracted", # distracted
        "8": "default", # shake head
        "9": "default",
        "10": "default",
        "11": "default",
        }]

@app.route("/service/poses", methods=["GET"])
def get_poses():
    return jsonify(poses), 201

@app.route("/service/poses", methods=["POST"])
def initialize_poses():
    if not request.json:
        abort(400)
    pose = {
        "thumbsup": "thumbsup",
        "clapping": "clapping",
        "0": "default",  
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
    poses.append(pose)
    return jsonify(poses), 201
    # Run this to add the user"s "button to pose" mapping
    # curl -i -H "Content-Type: application/json" -X POST -d '{"0":"default", "1":"", "2":""}' http://127.0.0.1:5000/service/poses

#########################################################################################################
# Pixel Settings
"""DELETE JSON INSIDE SETTINGS WHEN DEPLOYING SERVICE"""
# settings = []
settings = [{
        "os": "macbook pro 13-inch",
        "button_next_to_stop_vid": "170, 860",
        "vb_settings": "270, 780",
        "exit_settings": "345, 152",
        "reactions": "1039, 870",
        "thumbsup": "1058, 815",
        "clapping": "1020, 817",
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

@app.route("/service/settings", methods=["GET"])
def get_settings(): # all settings on local server
    return jsonify(settings), 201
    
@app.route("/service/settings", methods=["POST"])
def initialize_settings():
    if not request.json:
        abort(400)
  
    setting = {
        "os": request.json["os"],
        "button_next_to_stop_vid": request.json["button_next_to_stop_vid"],
        "vb_settings": request.json["vb_settings"],
        "exit_settings": request.json["exit_settings"],
        "reactions": request.json["reactions"],
        "thumbsup": request.json["thumbsup"],
        "clapping": request.json["clapping"],
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
    # curl -i -H "Content-Type: application/json" -X POST -d '{"os":"", "button_next_to_stop_vid":""}' http://127.0.0.1:5000/service/settings

if __name__ == "__main__":
    app.run(debug=True)

