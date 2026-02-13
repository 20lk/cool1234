import iss_speed
#to call iss_speed function, it is "iss_speed.get_speed('x','y')", where x and y are file names are the same format as this example 'atlas_photo_012.jpg'

from picamzero import Camera

cam = Camera()

from pathlib import Path
base_folder = Path(__file__).parent.resolve()

from datetime import datetime, timedelta
from time import sleep


start_time = datetime.now()
now_time = datetime.now()


def get_avg_speed(speeds):
    total = 0
    for speed in speeds:
        total += speed
    avg_speed = total/len(speeds)
    return avg_speed

def fivesf(num):
    out = 0
    if num % 10 == num:
        out = round(num, 4)
    elif num % 100 == num:
        out = round(num, 3)
    elif num % 1000 == num:
        out = round(num, 2)
    
    return out
#code start
#cam.take_photo("image1.jpg")
#cam.take_photo("image2.jpg")
    

data_file = base_folder / "result.txt"

#code finish
seconds = 0
photos = []
pair = []
count = 0

speeds = []
avg_speed = 0
while (now_time <= start_time + timedelta(minutes=9)):
    if seconds != int((now_time - start_time).total_seconds()):
        seconds = int((now_time - start_time).total_seconds())
        print(seconds)
        # run code here

        # imagine u take a photo
        if (seconds % 15 == 0): # runs every 5 seconds
            print("taking photo")
            cam.take_photo(f"image{count}.jpg")
            pair.append(f"image{count}.jpg")
            count += 1

        if len(pair) == 2: # pair finished
            photos.append(pair)

            speed = iss_speed.get_speed(pair[0], pair[1])
            speeds.append(speed)
            print(speed)
            avg_speed = get_avg_speed(speeds)


            with open(data_file, "w", buffering=1) as f:
                f.write(f"{fivesf(avg_speed)}")

            pair = []

    # Update the current time
    now_time = datetime.now()
# Out of the loop — stopping
print(photos)
print(avg_speed)
print(speeds)