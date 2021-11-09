
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
from time import strftime, sleep
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
    cs = cs_pin,
    dc = dc_pin,
    rst = reset_pin,
    baudrate = BAUDRATE,
    width=135,
    height = 240,
    x_offset = 53,
    y_offset = 40,
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

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

repeats = 0
detected = 0
dt = ""

while(True):
    y = top + 20
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print("I think its a:",labels[np.argmax(prediction)])

    if (1 == np.argmax(prediction)):
        detected = 1
        draw.text((x + 20, y), "LEAVING DETECTED", font=font, fill="#FF0000")
        repeats += 1
        if repeats < 4: 
            os.system('flite -voice st -t "Please go back to sleep. It is still late at night."')
            sleep(1)
        #print(strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
        else:
            y += 20
            dt = strftime("%m/%d %H:%M:%S")
            draw.text((x + 20, y), "last detected: ", font=font, fill="#FFFF00")
            y += 20
            draw.text((x + 20, y), dt, font=font, fill="#FFFF00")
    else:
        repeats = 0
        draw.text((x + 20, y), "No Activity Detected", font=font, fill="#00FF00")
        if detected == 1:
            y += 20
            draw.text((x + 20, y), "last detected: ", font=font, fill="#FFFF00")
            y += 20
            draw.text((x + 20, y), dt, font=font, fill="#FFFF00") 
    disp.image(image, rotation)

    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
