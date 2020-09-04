"""Pixel Settings"""
import pyautogui as py
import numpy as np
import requests
import json

class PixelSettings:

    def __init__(self):
        self.computer = 'mac'
        with open("user_data/pixel_settings.json", 'r') as file:
            def as_float(settings):
                if settings["x"] != "":
                    settings["x"] = int(float(settings["x"]))
                if settings["y"] != "":
                    settings["y"] = int(float(settings["y"]))
                return settings
            settings = json.load(file, object_hook=as_float)
            self.button_next_to_stop_vid = (settings[0]["x"], settings[0]["y"])
            self.vb_settings = (settings[1]["x"], settings[1]["y"])
            self.exit_settings = (settings[2]["x"], settings[2]["y"])
            self.pos0 = (settings[3]["x"], settings[3]["y"])
            self.pos1 = (settings[4]["x"], settings[3]["y"])
            self.pos2 = (settings[5]["x"], settings[3]["y"])
            self.pos3 = (settings[6]["x"], settings[3]["y"])
            self.pos4 = (settings[3]["x"], settings[7]["y"])
            self.pos5 = (settings[4]["x"], settings[7]["y"])
            self.pos6 = (settings[5]["x"], settings[7]["y"])
            self.pos7 = (settings[6]["x"], settings[7]["y"])
            self.pos8 = (settings[3]["x"], settings[8]["y"])
            self.pos9 = (settings[4]["x"], settings[8]["y"])
            self.pos10 = (settings[5]["x"], settings[8]["y"])
            self.pos11 = (settings[6]["x"], settings[8]["y"])
            self.reactions = (settings[9]["x"], settings[9]["y"])
            self.thumbsup = (settings[10]["x"], settings[10]["y"])
            self.clapping = (settings[11]["x"], settings[11]["y"])
            self.vb_grid = np.vstack([self.pos0, self.pos1, self.pos2, self.pos3, 
                                    self.pos4, self.pos5, self.pos6, self.pos7, 
                                    self.pos8, self.pos9, self.pos10, self.pos11])                 
        
    def stop_video(self):
        if "mac" in self.computer:
            py.hotkey('command', 'shift', 'v') # stop video
        elif "windows" in self.computer:
            py.hotkey('alt', 'shift', 'v') # stop video
        
    def click_arrow_to_right_stop_vid(self):
        py.click(self.button_next_to_stop_vid[0],self.button_next_to_stop_vid[1])  # click on arrow on the right of stop video

    def click_vb_settings(self):
        py.click(self.vb_settings[0],self.vb_settings[1]) # open virtual background settings

    def click_VB(self, button): # position of video in zoom e.g. 0 maps to none
        py.click(self.vb_grid[button][0], self.vb_grid[button][1])

    def click_exit_settings(self):
        py.click(self.exit_settings[0],self.exit_settings[1]) # click red x to settings
    
    def click_reactions(self):
        py.click(self.reactions[0],self.reactions[1]) # click on reactions
    
    def click_thumbsup(self):
        py.click(self.thumbsup[0],self.thumbsup[1]) # click thumbsup
    
    def click_clapping(self):
        py.click(self.clapping[0],self.clapping[1]) # click clapping
        
