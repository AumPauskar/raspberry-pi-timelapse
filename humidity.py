import time
import adafruit_dht
import board
import csv
from datetime import datetime

dht_device = adafruit_dht.DHT11(board.D4)

def initialize_csv():
    # Open the CSV file in write mode ('w') so the file is created if it doesn't exist
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Current datetime", "Temperature (C)", "Humidity (%)"])
        
def check_humidity():
    # Open the CSV file in append mode ('a') so data is added at the end
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        try:
            now = datetime.now()
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dht_device.humidity

            # Write the data into the CSV file
            writer.writerow([now, temperature_c, humidity])
            return "Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity)


        except RuntimeError as err:
            print(err.args[0])
            return "Temp:{} C / {} F    Humidity: {}%".format(-1, -1, -1)


        


def main():
    pass
if __name__ == "__main__":
    main()