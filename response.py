import os
from change_vb import changeVB
import time # DELETE when deploy

def response(post):
    request = changeVB()
    position = post["position"]
    mode = post["mode"]
    vid_length = post["vid_length"]
    # Test the pixel settings
    if position == 'stop_video':
        request.ps.stop_video()
    elif position == 'click_arrow_to_right_stop_vid':
        request.ps.click_arrow_to_right_stop_vid()
    elif position == 'click_vb_settings':
        request.ps.click_vb_settings()
    elif mode == 'click_VB':
        request.ps.click_VB(int(position))
    elif position == 'click_exit_settings':
        request.ps.click_exit_settings()
    elif position == 'click_reactions':
        request.ps.click_reactions()
    elif position == 'click_thumbsup':
        request.ps.click_thumbsup()
    elif position == 'click_clapping':
        request.ps.click_clapping()
    # Run the position and mode
    elif mode == 'thumbsup': 
        request.thumbsup()
    elif mode == 'clapping':
        request.clapping()
    elif mode == 'default' or mode == 'none':
        request.default(int(position))
    elif mode == 'distracted':
        request.distracted(int(position), int(vid_length))
    elif mode == 'action':
        request.action(int(position), int(vid_length))

        
    
