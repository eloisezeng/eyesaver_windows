# EyeSaver WindowsOS Automation Package

These scripts automate your computer to change your virtual background on Zoom. Download the EyeSaver WebApp so you can run these scripts when you press a button.

Main Advantages
---------------
- Appear to stare at the screen when your eyes are taking a break, or if you're doing something else
- Don't need to manually click the tiny buttons on Zoom

How to use EyeSaver: For Non-technical People
---------------
## Installation
### Prerequisites
Install Node.js <br> Install Git <br> Install Python <br>
### Windows OS
Copy this into your Powershell to install everything you need to run EyeSaver. 

git clone https://github.com/eloisezeng/eyesaver_windows <br>
cd eyesaver_windows <br>
pip3 install -r requirements.txt <br>
cd .. <br>
git clone https://github.com/eloisezeng/eyesaver_website <br>
cd eyesaver_website <br>
npm install <br>
cd .. <br>

## How to launch the desktop app
Run this command in Powershell for WindowsOS: <br>
cd eyesaver_windows; python3 local_server.py & cd .. && cd eyesaver_website ; npm start <br><br>
Search the website, 192.168.X.X:3000 (ip address of your computer), on your mobile device
### Find ip address on WindowsOS 
Search for Wifi-Settings. Click Hardware properties. You should see your IP address (192.168.X.X) next to IPv4 address.

#### Close the Powershell when you want to shut down the webapp (no longer be able to access 192.168.X.X:3000)

For Technical People
---------------
Install Requirements
---------------
pip install -r requirements.txt

Interested in the code?
---------------
- change_vb.py has functions that change the virtual background or do reactions (thumbsup/clapping)
- pixel_settings.py has functions that click certain positions on the screen. Users can change them in their code or in their computer app
- response.py is a python script that controls mouse clicking and key presses
- local_server.py is the server that runs response.py when a user presses a button

Contact
---------------
eyesaver@gmail.com

