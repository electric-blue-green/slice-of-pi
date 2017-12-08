import time
import scrollphathd
from scrollphathd.fonts import font3x5
from envirophat import light, weather, motion, analog
##  Welcome
print("""
Slice-Of-Pi
Made by @electric-blue-green
""")
##  Var setup
DISPLAY_BAR = True
disp = 0
## Light Level Def
def find_light_level():
    if int(light.light()) < 3:
        light_level = 0.01
    elif int(light.light()) < 7:
        light_level = 0.02
    elif int(light.light()) < 10:
        light_level = 0.03
    elif int(light.light()) < 13:
        light_level = 0.04
    elif int(light.light()) < 15:
        light_level = 0.05
    elif int(light.light()) < 17:
        light_level = 0.06
    elif int(light.light()) < 20:
        light_level = 0.07
    elif int(light.light()) < 22:
        light_level = 0.08
    elif int(light.light()) < 25:
        light_level = 0.09
    elif int(light.light()) < 27:
        light_level = 0.1
    elif int(light.light()) < 30:
        light_level = 0.12
    elif int(light.light()) < 35:
        light_level = 0.13
    elif int(light.light()) < 40:
        light_level = 0.14
    elif int(light.light()) < 45:
        light_level = 0.15
    elif int(light.light()) < 50:
        light_level = 0.16
    elif int(light.light()) < 55:
        light_level = 0.17
    elif int(light.light()) < 60:
        light_level = 0.18
    elif int(light.light()) < 70:
        light_level = 0.19
    elif int(light.light()) < 80:
        light_level = 0.2
    elif int(light.light()) < 90:
        light_level = 0.21
    elif int(light.light()) < 100:
        light_level = 0.22
    elif int(light.light()) < 120:
        light_level = 0.23
    elif int(light.light()) < 140:
        light_level = 0.24
    elif int(light.light()) < 160:
        light_level = 0.25
    elif int(light.light()) < 180:
        light_level = 0.26
    elif int(light.light()) < 200:
        light_level = 0.27
    elif int(light.light()) < 220:
        light_level = 0.28
    elif int(light.light()) < 240:
        light_level = 0.29
    elif int(light.light()) < 260:
        light_level = 0.3
    elif int(light.light()) < 280:
        light_level = 0.32
    elif int(light.light()) < 300:
        light_level = 0.34
    elif int(light.light()) < 350:
        light_level = 0.36
    elif int(light.light()) < 400:
        light_level = 0.38
    elif int(light.light()) < 450:
        light_level = 0.4
    elif int(light.light()) < 500:
        light_level = 0.42
    elif int(light.light()) < 550:
        light_level = 0.44
    elif int(light.light()) < 600:
        light_level = 0.46
    elif int(light.light()) < 700:
        light_level = 0.48
    elif int(light.light()) < 800:
        light_level = 0.5
    elif int(light.light()) < 900:
        light_level = 0.55
    elif int(light.light()) < 1000:
        light_level = 0.6
    elif int(light.light()) < 1200:
        light_level = 0.65
    elif int(light.light()) < 1400:
        light_level = 0.7
    elif int(light.light()) < 1600:
        light_level = 0.75
    elif int(light.light()) < 1800:
        light_level = 0.8
    elif int(light.light()) < 2000:
        light_level = 0.85
    elif int(light.light()) < 2500:
        light_level = 0.9
    elif int(light.light()) < 3000:
        light_level = 0.95
    else:
        light_level = 1
    return light_level
##  Disp Switch Def                     ! NOT WORKING
def main(disp):
    get_disp_time(disp)
def get_disp_time(disp):
    disp = 0
    time.sleep(3)
    print("Disp set to time")
    get_disp_date(disp)
    return
def get_disp_date(disp):
	disp = 1
	time.sleep(3)
	print("Disp set to date")
	get_disp_time(disp)
#main(disp)
##  Clock
while True:
    print("disp: ", disp)
    while True:
        scrollphathd.clear()
        #!debug#print(find_light_level())
        # Convert seconds -> percent
        float_sec = (time.time() % 60) / 59.0
        # spread percentage over bar
        seconds_progress = float_sec * 15
        if DISPLAY_BAR:
            # draw seconds bar
            for y in range(15):
                BRIGHTNESS = 1
                # adjust brigtness
                current_pixel = min(seconds_progress, 1)
                scrollphathd.set_pixel(y + 1, 6, current_pixel * find_light_level())
                seconds_progress -= 1
                if seconds_progress <= 0:
                    break
        else:
            # just a dot
            scrollphathd.set_pixel(int(seconds_progress), 6, find_light_level())
        # format time
        scrollphathd.write_string(
            time.strftime("%H:%M"),
            x=0, # Align to the left of the buffer
            y=0, # Align to the top of the buffer
            font=font3x5, # Use the font3x5 font we imported above
            brightness=find_light_level() # Use our global brightness value
        )
        # tick between 0 and 1
        if int(time.time()) % 2 == 0:
            scrollphathd.clear_rect(8, 0, 1, 5)
        # Display, and refresh
        scrollphathd.show()
        time.sleep(0.01)
while True:
    print(int(time.time()) % 4)