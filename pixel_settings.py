"""Pixel Settings"""
import pyautogui as py
import numpy as np
import requests

class PixelSettings:

    def __init__(self, settings):
        self.os = settings["os"]
        self.button_next_to_stop_vid = settings["button_next_to_stop_vid"].split(", ")
        self.button_next_to_stop_vid = [int(i) for i in self.button_next_to_stop_vid]
        self.vb_settings = settings["vb_settings"].split(", ")
        self.vb_settings = [int(i) for i in self.vb_settings]
        self.exit_settings = settings["exit_settings"].split(", ")
        self.exit_settings = [int(i) for i in self.exit_settings]
        self.reactions = settings["reactions"].split(", ")
        self.reactions = [int(i) for i in self.reactions]
        self.clapping = settings["clapping"].split(", ")
        self.clapping = [int(i) for i in self.clapping]
        self.thumbsup = settings["thumbsup"].split(", ")
        self.thumbsup = [int(i) for i in self.thumbsup]
        self.pos0 = settings["0"].split(", ")
        self.pos1 = settings["1"].split(", ")
        self.pos2 = settings["2"].split(", ")
        self.pos3 = settings["3"].split(", ")
        self.pos4 = settings["4"].split(", ")
        self.pos5 = settings["5"].split(", ")
        self.pos6 = settings["6"].split(", ")
        self.pos7 = settings["7"].split(", ")
        self.pos8 = settings["8"].split(", ")
        self.pos9 = settings["9"].split(", ")
        self.pos10 = settings["10"].split(", ")
        self.pos11 = settings["11"].split(", ")
        self.vb_grid = np.vstack([self.pos0, self.pos1, self.pos2, self.pos3, 
                                  self.pos4, self.pos5, self.pos6, self.pos7, 
                                  self.pos8, self.pos9, self.pos10, self.pos11])
        self.vb_grid = self.vb_grid.astype(np.int)
    
    def stop_video(self):
        if self.os == 'macbook pro 13-inch':
            py.hotkey('command', 'shift', 'v') # stop video
        elif self.os == 'windows':
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
        
