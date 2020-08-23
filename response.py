import os
from change_vb import changeVB
import time # DELETE when deploy

def response(user_request_mapping, button, settings):
    request = changeVB(settings)
    time.sleep(1) # DELETE when deploy
    # Test the pixel settings
    if button == 'stop_video':
        request.ps.stop_video()
    elif button == 'click_arrow_to_right_stop_vid':
        request.ps.click_arrow_to_right_stop_vid()
    elif button == 'click_vb_settings':
        request.ps.click_vb_settings()
    elif button == 'click_VB':
        request.ps.click_VB(int(button)) # how do we know button?
    elif button == 'click_exit_settings':
        request.ps.click_exit_settings()
    elif button == 'click_reactions':
        request.ps.click_reactions()
    elif button == 'click_thumbsup':
        request.ps.click_thumbsup()
    elif button == 'click_clapping':
        request.ps.click_clapping()
    # Run the button
    elif button == 'thumbsup': 
        request.thumbsup()
    elif button == 'clapping':
        request.clapping()
    elif user_request_mapping[button] == 'default':
        request.default(int(button))
    elif user_request_mapping[button] == 'distracted':
        request.distracted(int(button))

        
    
