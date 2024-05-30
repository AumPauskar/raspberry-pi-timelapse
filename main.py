import time
import os
import json
from humidity import check_humidity, initialize_csv
# Load the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    delay = int(config["delay"]) - 5
    duration = config["duration"]
    try:
        specified_time, format = duration.split(" ")
        if format == "day":
            duration = int(specified_time) * 86400
        elif format == "hr":
            duration = int(specified_time) * 3600
        elif format == "min":
            duration = int(specified_time) * 60
        elif format == "sec":
            duration = int(specified_time)
    except ValueError:
        print("Please specify the time in the following format (config.json)")
        print('''
              day: for 1day or multiple days
              hr: for 1hour or multiple hours
              min: for 1minute or multiple minutes
              sec: for 1second or multiple seconds
              ''')
        exit()
    # duration = int(config["duration"]) * 60

pic_name = 1

def take_photo():
    global pic_name
    os.system(f"libcamera-still --nopreview -o timelapse/timelapse{pic_name}.jpg --vflip")
    pic_name += 1
    print(pic_name,"picture taken suncessfully")
    print("Current ambience: ", check_humidity())

def timelapse(delay, duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        take_photo()
        time.sleep(delay)
        print(start_time - end_time, "time remaining")

def main():
    initialize_csv()
    timelapse(delay, duration)

if __name__ == "__main__":
    main()
