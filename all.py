#test
#!/usr/bin/env python

import time

import scrollphathd
from scrollphathd.fonts import font3x5
from envirophat import light, weather, motion, analog

print("""
Slice-Of-Pi
Made by @electric-blue-green
""")

##  --  Scrollphat Setup
# 0 ->  10  ->  50  ->  150  ->  200  ->  400  ->  800  ->  1200  ->  2000  ->  3000  ->  5000  ->  10000  ->  max
#   0.5     0.1     0.2     0.25      0.3      0.4      0.5       0.6       0.7       0.8       0.9         1
# 0 ->  5  ->  50  ->  150  ->  200  ->  400  ->  800  ->  1200  ->  2000  ->  3000  ->  5000  ->  10000  ->  max
#0-3        0.01
#3-7        0.02
#7-10       0.03
#10-15      0.04
#15-20      0.05
#20-25      0.06
#25-30      0.07
#35-40      0.08
#40-45      0.09
#45-50      0.1
#50-55      0.12
#55-60      0.13
#60-70      0.15
#70-80      0.16
#80-90      0.17
#90-100     0.18
#100-120    0.20
#120-140    0.22
#140-160    0.23
#160-200    0.25
#200-250    0.26
#250-300    0.28
#300-350    0.3
#350-400    0.35
#400-450    0.4
#450-500    0.45
#500-600    0.5
#600-700    0.55
#700-800    0.6
#800-900    0.65
#900-1000   0.75
#1000-1200  0.85
#1200-1500  0.95
#1500-2000  1
#2000-3000
#3000-4000
#4000-max
#
#
#
#
DISPLAY_BAR = True
disp = 0
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

while True:
    print("disp: ", disp)
    while True:
        scrollphathd.clear()
        #print(find_light_level())
        # Grab the "seconds" component of the current time
        # and convert it to a range from 0.0 to 1.0
        float_sec = (time.time() % 60) / 59.0

        # Multiply our range by 15 to spread the current
        # number of seconds over 15 pixels.
        #
        # 60 is evenly divisible by 15, so that
        # each fully lit pixel represents 4 seconds.
        #
        # For example this is 28 seconds:
        # [x][x][x][x][x][x][x][ ][ ][ ][ ][ ][ ][ ][ ]
        #  ^ - 0 seconds                59 seconds - ^
        seconds_progress = float_sec * 15

        if DISPLAY_BAR:
            # Step through 15 pixels to draw the seconds bar
            for y in range(15):
                BRIGHTNESS = 1
                # For each pixel, we figure out its brightness by
                # seeing how much of "seconds_progress" is left to draw
                # If it's greater than 1 (full brightness) then we just display 1.
                current_pixel = min(seconds_progress, 1)

                # Multiply the pixel brightness (0.0 to 1.0) by our global brightness value
                scrollphathd.set_pixel(y + 1, 6, current_pixel * find_light_level())

                # Subtract 1 now we've drawn that pixel
                seconds_progress -= 1

                # If we reach or pass 0, there are no more pixels left to draw
                if seconds_progress <= 0:
                    break

        else:
            # Just display a simple dot
            scrollphathd.set_pixel(int(seconds_progress), 6, find_light_level())

        # Display the time (HH:MM) in a 5x5 pixel font
        #print(find_light_level())
        scrollphathd.write_string(
            time.strftime("%H:%M"),
            x=0, # Align to the left of the buffer
            y=0, # Align to the top of the buffer
            font=font3x5, # Use the font3x5 font we imported above
            brightness=find_light_level() # Use our global brightness value
        )

        # int(time.time()) % 2 will tick between 0 and 1 every second.
        # We can use this fact to clear the ":" and cause it to blink on/off
        # every other second, like a digital clock.
        # To do this we clear a rectangle 8 pixels along, 0 down,
        # that's 1 pixel wide and 5 pixels tall.
        if int(time.time()) % 2 == 0:
            scrollphathd.clear_rect(8, 0, 1, 5)

        # Display our time and sleep a bit. Using 1 second in time.sleep
        # is not recommended, since you might get quite far out of phase
        # with the passing of real wall-time seconds and it'll look weird!
        #
        # 1/10th of a second is accurate enough for a simple clock though :D
        scrollphathd.show()
        time.sleep(0.01)
