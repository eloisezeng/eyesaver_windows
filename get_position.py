from pynput import mouse

class getPositions():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def on_click(self, x, y, button, pressed):
        if not pressed: # if mouse isn't pressed anymore
            # Stop listener
            return False
        self.x = int(x)
        self.y = int(y)

    def mouse_listen(self):
        # Collect events until released
        with mouse.Listener(
                on_click=self.on_click) as listener:
            listener.join()
        return (self.x, self.y) # return pixels after mouse stopped listening

# a = getPositions()
# x, y = a.mouse_listen()
# print(x, y)
