import os
from change_vb import changeVB

def response(user_request_mapping, button, settings):
    request = changeVB(settings)
    if button == 'thumbsup': 
        request.thumbsup()
    elif button == 'clapping':
        request.clapping()
    elif user_request_mapping[button] == 'default':
        request.default(int(button))
    elif user_request_mapping[button] == 'distracted':
        request.distracted(int(button))


        
    
