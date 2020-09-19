import os
stream = os.popen('wmic computersystem get model')
print(stream.read()[6:].strip())