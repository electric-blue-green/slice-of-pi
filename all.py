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
DISPLAY_BAR = True
disp = 0
def find_light_level():
    if int(light.light()) < 10:
        light_level = 0.05
    elif int(light.light()) < 50:
        light_level = 0.1
    elif int(light.light()) < 150:
        light_level = 0.2
    elif int(light.light()) < 200:
        light_level = 0.25
    elif int(light.light()) < 400:
        light_level = 0.3
    elif int(light.light()) < 800:
        light_level = 0.4
    elif int(light.light()) < 1200:
        light_level = 0.5
    elif int(light.light()) < 2000:
        light_level = 0.6
    elif int(light.light()) < 3000:
        light_level = 0.7
    elif int(light.light()) < 5000:
        light_level = 0.8
    elif int(light.light()) < 10000:
        light_level = 1
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
