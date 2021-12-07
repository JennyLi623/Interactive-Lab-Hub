import paho.mqtt.client as mqtt
import uuid
import os

import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

BAUDRATE = 64000000

spi = board.SPI()

disp = st7789.ST7789(
    spi, 
    cs=cs_pin,
    dc=dc_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

height = disp.width
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

padding = -2
top = padding
bottom = height - padding

x = 0
y = top + 20

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)

buttonA.switch_to_input()
buttonB.switch_to_input()

topic = 'IDD/#'

received = False

def on_connect(client, userdata, flags, rc):
    #print(f"connected with reult code {rc}")
    client.subscribe(topic)
    received = False

def on_message(client, userdata, msg):
    #print(f"topic: {msg, topic} msg: {msg.payload.decode('UTF-8')}")
    global received
    if msg.topic == 'IDD/detect' and received == False:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FF0000")
        draw.rectangle((10,10, width-20, height-20), outline=0, fill=0)
        draw.text((x + 20, y + 30), "    ALERT", font=font, fill="#FF0000")
        draw.text((x + 20, y + 50), "Man fallen on ground", font=font, fill="#FF0000")
        disp.image(image, rotation)
        print("man fall")   
        os.system('flite -voice st -t "Alert! The person may have fallen!"')
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        disp.image(image, rotation)

    if buttonB.value and not buttonA.value:
        #print("button clicked")
        received = True
        client.publish("IDD/response", "back")
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        draw.text((x + 20, y + 30), "BE RIGHT BACK", font = font, fill="#00FF00")
        disp.image(image, rotation)
        os.system('flite -voice st -t "Alarm received"')

    if buttonA.value and not buttonB.value:
        #print("button clicked")
        received = True
        client.publish("IDD/response", "police")
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        draw.text((x + 20, y + 30), "CALL FOR HELP", font = font, fill="#FFFF00")
        disp.image(image, rotation)
        os.system('flite -voice st -t "Alarm received"')

client = mqtt.Client(str(uuid.uuid1()))

client.tls_set()

client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_forever()
