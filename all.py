#!/usr/bin/env python

import time

import scrollphathd
from scrollphathd.fonts import font3x5
from envirophat import light, weather, motion, analog

print("""
Scroll pHAT HD: Clock
Displays hours and minutes in text,
plus a seconds progress bar.
Press Ctrl+C to exit!
""")

##  --  Scrollphat Setup
DISPLAY_BAR = True
while True:
    if int(light.light()) < 1000:
        BRIGHTNESS = int(int(light.light())/1000)
    else:
        BRIGHTNESS = 1
while True:
    scrollphathd.clear()
    float_sec = (time.time() % 60) / 59.0               #   Seconds
    seconds_progress = float_sec * 15                   #   Spread progress bar
    if DISPLAY_BAR:
        for y in range(15):
            current_pixel = min(seconds_progress, 1)
            scrollphathd.set_pixel(y + 1, 6, current_pixel * BRIGHTNESS)
            seconds_progress -= 1
            if seconds_progress <= 0:
                break
    else:
        scrollphathd.set_pixel(int(seconds_progress), 6, BRIGHTNESS)
        scrollphathd.write_string(
            time.strftime("%H:%M"),
            x=0, # Align to the left of the buffer
            y=0, # Align to the top of the buffer
            font=font3x5, # Use the font3x5 font we imported above
            brightness=BRIGHTNESS # Use our global brightness value
        )
    if int(time.time()) % 2 == 0:
        scrollphathd.clear_rect(8, 0, 1, 5)
    scrollphathd.show()
    time.sleep(0.1)
