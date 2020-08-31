"""
Server manages user data and requests.
User presses button to request a pose. Server calls response.py."""
from flask import Flask, jsonify, abort, request
from response import response 
import urllib, json
import requests
from flask_cors import CORS, cross_origin

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
# @cross_origin()
def request_pose(): # Request
    if not request.json: # or not "button" in request.json:
        abort(400)
    post = {
        "position": request.json["position"],
        "mode": request.json["mode"]
    }
    url_settings = "http://127.0.0.1:5000/settings"
    settings = requests.get(url_settings)
    settings = settings.json()[-1]
    response(post, settings) # action
    posts.append(post) # see post on website
    return jsonify(posts), 201
    # Run this to add a post
    # curl -i -H "Content-Type: application/json" -X POST -d '{"button":"0"}' http://127.0.0.1:5000/posts

#########################################################################################################
# Pixel Settings
"""DELETE JSON INSIDE SETTINGS WHEN DEPLOYING SERVICE"""
# settings = []
settings = [{
        "computer": "macbook pro 13-inch",
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

@app.route("/settings", methods=["GET"])
def get_settings(): # all settings on local server
    return jsonify(settings), 201
    
@app.route("/settings", methods=["POST"])
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
    # curl -i -H "Content-Type: application/json" -X POST -d '{"os":"", "button_next_to_stop_vid":""}' http://127.0.0.1:5000/settings

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

