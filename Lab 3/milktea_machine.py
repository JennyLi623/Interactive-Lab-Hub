import speech2text
import os
import digitalio
import busio
import adafruit_apds9960.apds9960
import board
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
import random

i2c = busio.I2C(board.SCL, board.SDA)
card_sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

card_sensor.enable_proximity = True

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

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
y = top + 20
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
colors = ["#f4b6c2", "#0336cc", "#fe8a71", "#fad9c1"]
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)

buttonA.switch_to_input()
buttonB.switch_to_input()
size = 18
inc = True


flavor_list = {1: "original", 2: "matcha", 3: "strawberry"}
flavor_price = {"original": 4.99, "matcha": 5.99, "strawberry": 6.99}
sweetness_display={1: "0% sweetness", 2: "50% sweetness", 3: "100% sweetness"}
sweetness={1: "zero sweetness", 2: "fifty percent sweetness", 3: "one hundred percent sweetness"}
ice_level={1: "no ice", 2: "less ice", 3: "full ice"}
addons={1: "boba", 2: "pudding", 3: "aloe", 4: "cream foam"}
addon_price= {"boba": 0.25, "pudding": 0.25, "aloe": 0.5, "cream foam": 1}




def text2voice(phrase, l, choice = 0):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    y = top + 20
    if choice == 1:
        for c, i in enumerate(l.values()):
            draw.text((x, y), i, font=font, fill=colors[c])
            y += 22
    else:
        for c, i in enumerate(l.values()):
            print(i)
            draw.text((x, y), str(c + 1) + "....." + i, font=font, fill=colors[c])
            y += 22
    disp.image(image, rotation)
    os.system('flite -voice slt -t ' + phrase)

def voice2num():
    os.system('arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav')
    l = speech2text.get_word()
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
    for i in l:
        if i in num_dict.keys():
            return num_dict[i]
    return 1

class Milktea:
    def __init__(self, flavor):
        self.flavor = flavor
        self.sweetness = 100
        self.ice_level = "full ice"
        self.addon = set()
        self.price = flavor_price[flavor]

    def add_addon(self, input):
        input = addons[input]
        if input in addons.values():
            self.addon.append(addons[input])
        self.price += addon_price[addons[input]]

class Customer:
    amount = 0

    def __init__(self):
        self.items = []

    def add_items(self):
        global text2voice
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x + 20, y), "Received!", font = font, fill = "#00FF00")
        disp.image(image, rotation)
        text2voice('"Received! Now please select the milktea you want by telling me the number on the screen."', flavor_list)
        get_milktea = voice2num()
        new_cup = Milktea(flavor_list[get_milktea])
        print(get_milktea)
        text2voice('\"You ordered ' + new_cup.flavor + ' milktea. Now please select the sweetness you want by telling me the number on the screen.\"', sweetness_display)
        get_sweetness = voice2num()
        new_cup.sweetness = sweetness[get_sweetness]
        text2voice('\"You ordered ' + new_cup.sweetness + '. Now please select the ice level you want by telling me the number on the screen.\"', ice_level)
        get_icelevel = voice2num()
        new_cup.ice_level = ice_level[get_icelevel]  
        text2voice('\"You ordered ' + new_cup.ice_level + '\"', {}, 1)
        choice = -1
        while choice != 0:
            text2voice('"Now please select the addons by telling the number. Say zero to finish adding the addons."', addons)
            choice = voice2num()
            if choice == 0:
                break
            new_cup.addon.add(addons[choice])
            text2voice('\"You ordered ' + addons[choice] + '\"', {}, 1)
        text2voice('"Now preparing your milkea."', {1: 'PROCESSING'}, 1)
        text2voice('"Your milktea is ready. Please grab it on the right side of the machine."', {1: '=====>'}, 1)

def start():
    text2voice('"Hello, I am the Auto milktea machine. Please insert your card to begin!"', {1: "BOBA", 2:"Milktea Shop"}, 1)
    print(card_sensor.proximity)
    while card_sensor.proximity < 100:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x + 20, y), "Insert card", font = font, fill = "#FF0000")
        disp.image(image, rotation)
        print(card_sensor.proximity)
    customer = Customer()
    customer.add_items()
        
start()
#while True:
    #info = input()
