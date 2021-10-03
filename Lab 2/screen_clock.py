import time
from time import strftime, sleep
import random
import subprocess
import digitalio
import busio
import adafruit_apds9960.apds9960
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

i2c = busio.I2C(board.SCL, board.SDA)
phone_sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

phone_sensor.enable_proximity = True

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)

buttonA.switch_to_input()
buttonB.switch_to_input()
size = 18
inc = True
phone_on_sensor = False
phone_hint_1 = "Put Your Phone"
phone_hint_2 = "DDDOOOWWWNNN"
study_mode = False
study = False
timer = 0

while True:
    # Draw a black filled box to clear the image.
    if timer == 0:
        study = not study
        if study:
            timer = 250
        else:
            timer = 50
    if study_mode:
        if study and phone_on_sensor:
            timer -= 1
            draw.rectangle((0, 0, width, height), outline = 0, fill = "#FF0000")
            draw.rectangle((0, 0, int(width - width * timer / 250), height), outline = 0, fill = "#00FF00")
        elif not study:
            draw.rectangle((0, 0, width, height), outline = 0, fill = "#0000FF")
            draw.rectangle((0, 0, int(width - width * timer / 50), height), outline = 0, fill = "#FF0000")
            timer -= 1
        else:
            draw.rectangle((0, 0, width, height), outline=0, fill = "#FF0000")
            draw.rectangle((10, 10, width - 10, height - 10), outline=0, fill = "#000000")
    else:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
    display_time = 0.1

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    if size == 24:
        inc = False
    elif size == 18:
        inc = True
    if inc == True:
        size += 1
    else:
        size -= 1
    quotefont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    timefont = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    y = top + 20
    quotes = ["Believe in yourself", "work hard", "Be a dreamer", "Take action", "Set big goals"]
    colors = ["#f4b6c2", "#0336cc", "#fe8a71", "#fad9c1", "#ff0000"]
    time_left = "Time Left: " + str(int(timer / 10)) + "min"
    display = strftime("%m/%d/%y %H:%M:%S")
    if phone_sensor.proximity != 0:
        phone_on_sensor = True
        phone_hint_1 = "Keep on the good work"
    else:
        phone_on_sensor = False
        phone_hint_1 = "Put Your Phone"


    if buttonA.value and buttonB.value:
        if study_mode and phone_on_sensor:
            draw.text((x, y), time_left, font = quotefont, fill = "#000000")
        elif study_mode and study and not phone_on_sensor:
            draw.text((x + 20, y), phone_hint_1, font = quotefont, fill = "#FF0000")
            y += 30
            draw.text((x + 20, y), phone_hint_2, font = quotefont, fill = "#FF0000")
        elif study_mode and not study:
           draw.text((x, y), time_left, font = quotefont, fill = "#000000") 
        else:
           draw.text((x, y), display, font=timefont, fill="#00FF00")
           y = top + 40
    elif buttonB.value and not buttonA.value:
        study_mode = not study_mode
        if study_mode:
            study = False
            timer = 0
    else:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, y), random.choice(quotes), font=quotefont, fill=random.choice(colors))
        display_time = 3
    # Display image.
    disp.image(image, rotation)
    time.sleep(display_time)
    
