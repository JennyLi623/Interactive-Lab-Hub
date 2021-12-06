import cv2
from collections import deque
import uuid
import paho.mqtt.client as mqtt
import time
import os
import qwiic
import time
import requests

#Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))

#configure network encryption etc
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect( 
    'farlab.infosci.cornell.edu',
    port = 8883)

topic = "IDD/detect"  
topic2 = 'IDD/response'
reset = 1
initial_delay = True

ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):
    print("Sensor online!\n")

# see how long we keep track of the a person.
# the longer the time_frame, the longer we get alert after people fall
time_frame = 20
alert_threshold = 500
same_people_threshold = 100
thres = 0.45 # Threshold to detect object

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

classNames= []
classFile = 'coco.names'
# with open(classFile,'rt') as f:
#     # print(f.read())
#     classNames = f.read()

file1 = open(classFile, 'r')
# count = 0


while True:

    # Get next line from file
    line = file1.readline()
 
    # # if line is empty
    # # end of file is reached
    if not line:
        break
    # print("Line{}: {}".format(count, line.strip()))
    classNames.append(line.strip())
 
file1.close()

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)



people = []
def same_people(a, b):
    dis = 0
    for i in range(len(a)):
        dis += abs(a[i]-b[i])
    return dis < same_people_threshold

def alert(people):
    for p in people:
        diff = [0,0,0,0]
        # print('printing', p[-1])
        if p[-1][0] == -1:
            continue
        for i in range(len(p)-1):
            diff += abs(p[i]-p[i+1])
            # print(diff)
        # print('difference', diff)
        # print(sum(diff))
        # print(len(p))
        if sum(diff) < alert_threshold and len(p)>= time_frame:
            client.publish(topic, "Alert!")
            p.append((-1,-1,-1,-1))
            print('ALERT')





import paho.mqtt.client as mqtt
import uuid

# # the # wildcard means we subscribe to all subtopics of IDD
# topic = 'IDD/#'


#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic2)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
    message = msg.payload.decode('UTF-8')
    if message == 'police':
        os.system('espeak -ven+f2 -k5 -s150 --stdout  "we are calling the police" | aplay')
    if message == 'back':
        os.system('espeak -ven+f2 -k5 -s150 --stdout  "The care giver is on the way" | aplay')
    # print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    # if msg.topic == 'IDD/response':
    #     print('in the if statement')
    #     print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
# client.on_connect = on_connect
# client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)
# client.loop_forever()

while True:
    try:
        ToF.start_ranging()
        distance = ToF.get_distance()
        ToF.stop_ranging()
        r = requests.get(url="https://lighting-backend.herokuapp.com/dtoc/" + "{:.2f}".format(distance / 100))
        print(r.json())
    except Exception as e:
        print(e)

    # print('Number of poeple', len(people))
    success,img = cap.read()
    
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    # print(classIds,bbox)
    
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            if classNames[classId-1] != 'person':
                continue
            add = False
            for p in people:
        
                last_pos = p[-1]
                if same_people(last_pos, box):
                    add = True
                    if p[-1][0] == -1:
                        p = []
                    p.append(box)
                    if len(p) > time_frame:
                        p.popleft()
                    # print('same people')
            if not add:
                p = deque()
                p.append(box)
                people.append(p)
            # print(box)
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        alert(people)
    cv2.imshow('Output',img)
    cv2.waitKey(1)

    client.on_connect = on_connect
    client.on_message = on_message  
    client.loop()
    # os.system('espeak -ven+f2 -k5 -s150 --stdout  "we are calling the police" | aplay')
    # os.system('espeak -ven+f2 -k5 -s150 --stdout  "The care giver is on the way" | aplay')
    # time.sleep(0.5)


# import cv2

# # Enable camera
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 420)

# # import cascade file for facial recognition
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# '''
#     # if you want to detect any object for example eyes, use one more layer of classifier as below:
#     eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
# '''

# while True:
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Getting corners around the face
#     faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  # 1.3 = scale factor, 5 = minimum neighbor
#     # drawing bounding box around face
#     for (x, y, w, h) in faces:
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

#     '''
#     # detecting eyes
#     eyes = eyeCascade.detectMultiScale(imgGray)
#     # drawing bounding box for eyes
#     for (ex, ey, ew, eh) in eyes:
#         img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)
#     '''

#     cv2.imshow('face_detect', img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyWindow('face_detect')
