"""Change virtual backgrounds or reactions when in zoom meetings"""
"""Used exact pixel position so not that good."""
import pyautogui as py
import time
from pixel_settings import PixelSettings

class changeVB: # change virtual background
    
    def __init__(self):
        self.ps = PixelSettings()

    def open_virt_settings(self): # open up settings to virtual background
        self.ps.click_arrow_to_right_stop_vid()
        time.sleep(0.2)
        self.ps.click_vb_settings()
        time.sleep(0.2)

    def thumbsup(self):
        self.ps.click_reactions() # click reactions button
        time.sleep(0.2)
        self.ps.click_thumbsup() # choose thumbsup

    def clapping(self):
        self.ps.click_reactions()
        time.sleep(0.2)
        self.ps.click_clapping() # choose clapping

    def default(self, position): # default commands of VB
        self.ps.stop_video()
        self.open_virt_settings()
        time.sleep(0.2)
        self.ps.click_VB(position)
        time.sleep(0.2)
        self.ps.click_exit_settings()

    def distracted(self, position, vid_length): # distraction
        self.open_virt_settings()
        time.sleep(0.2)
        self.ps.click_VB(position) # position of distracted VB
        time.sleep(vid_length) # length of distraction
        self.ps.stop_video()
        time.sleep(0.2)
        self.ps.click_VB(0) # click on none. 
        time.sleep(0.2)
        self.ps.click_exit_settings()

    def action(self, position, vid_length): # distraction
        self.open_virt_settings()
        time.sleep(0.2)
        self.ps.click_VB(position) # position of action VB
        time.sleep(vid_length) # length of action
        self.ps.click_default_pos() # click on default.
        time.sleep(0.2)
        self.ps.click_exit_settings()

    