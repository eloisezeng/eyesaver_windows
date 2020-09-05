import os
from cv2 import cv2

stream_ip = os.popen('ipconfig getifaddr en0') # gets ip address
ip = stream_ip.read().rstrip() # gets rid of newline
cmd_computer = "system_profiler SPHardwareDataType | grep  \'Model Identifier\'" 
# get model identifier of computer
# system_profiler SPHardwareDataType | grep "Model Identifier"
stream_computer = os.popen(cmd_computer)
computer = stream_computer.read().strip()
command_qr = "qrencode -o qrcode.png " + "\'ip: " + ip + " | " + computer + "\'" # use pipe so i can separate values
os.popen(command_qr) # run command in terminal
img = cv2.imread('qrcode.png')
cv2.imshow('Press q to exit image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()