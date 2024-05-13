import time
import os
import json

# Load the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    delay = int(config["delay"]) - 5
    duration = int(config["duration"]) * 60

pic_name = 1

def take_photo():
    global pic_name
    os.system(f"libcamera-still --nopreview -o timelapse/timelapse{pic_name}.jpg --vflip")
    pic_name += 1

def timelapse(delay, duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        take_photo()
        time.sleep(delay)

def main():
    timelapse(delay, duration)

if __name__ == "__main__":
    main()
