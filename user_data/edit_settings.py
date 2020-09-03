import json

def edit_setting(name, x, y):
    with open("pixel_settings.json", "r+") as file:
        data = json.load(file)
        cnt = 0
        for setting in data:
            if setting["name"] == name:
                break
            cnt += 1 # indice of object in data
        data[cnt]["x"] = x
        data[cnt]["y"] = y
        file.seek(0)  # rewind
        json.dump(data, file, indent=4)
        file.truncate()
edit_setting("click_arrow_to_right_stop_vid", "", "")
        