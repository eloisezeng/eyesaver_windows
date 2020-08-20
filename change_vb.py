"""Change virtual backgrounds or reactions when in zoom meetings"""
import pyautogui as py
import time
from pixel_settings import PixelSettings

class changeVB: # change virtual background
    
    def __init__(self, settings):
        self.ps = PixelSettings(settings)
        
    def initialize(self): # DELETE when it's an app
        time.sleep(1) 

    def open_virt_settings(self): # open up settings to virtual background
        self.initialize()
        self.ps.click_arrow_to_right_stop_vid()
        time.sleep(0.2)
        self.ps.click_vb_settings()
        time.sleep(0.2)

    def thumbsup(self):
        self.initialize()
        self.ps.click_reactions() # click reactions button
        time.sleep(0.2)
        self.ps.click_thumbsup() # choose thumbsup

    def clapping(self):
        self.initialize()
        self.ps.click_reactions()
        time.sleep(0.2)
        self.ps.click_clapping() # choose clapping

    def default(self, position): # default commands of VB
        time.sleep(1) # DELETE when deploying app (give time for me to switch over)
        self.ps.stop_video()
        self.open_virt_settings()
        self.ps.click_VB(position)
        time.sleep(0.2)
        self.ps.click_exit_settings()

    def distracted(self, position, vid_length=7): # distraction
        self.open_virt_settings()
        self.ps.click_VB(position) # position of distracted VB
        time.sleep(vid_length) # length of distraction
        self.ps.stop_video()
        time.sleep(0.2)
        self.ps.click_VB(0) # click on none. 
        time.sleep(0.2)
        self.ps.click_exit_settings()

    