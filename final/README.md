# Final Project
![Blue Clinical Friendly Vaccine Information General Health Poster (1)](https://user-images.githubusercontent.com/89815599/145864435-14387a19-85af-4192-a271-2799bb6f214f.gif)
Team member  **Jueying Li(jl2852)** and **Shengnan Han(sh2556)**

#### I.   Installation
***Try out our project!***

Requirements: Need two raspberry pi to communicate with each other.
1. For both raspberry pi:
 - Clone the repo
```
git clone https://github.com/JennyLi623/Interactive-Lab-Hub.git
```
 - Go to final directory
```
cd final
```
 - Create virtual environment and install dependencies
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
2. On one raspberry pi, namely PiA
 - Connect it with camera 
 - Place the camera where it can see the entire room
 - Then open VNC and run the command. This allow the camera to track the people’s movement and give alert when elder people are not moving for a while
```
python object_tracking.py
```
3. On another raspberry pi, namely PiB
 - Run the command. This allow the caregiver to receive alert from elder people and respond with messages by pressing the either one of the button on the screen of the PiB
```
python detect.py
```
4. Currently, the lighting is simulated using a website that connects to a backend which connects to a distance sensor. To show this effect, connect the distance sensor with Raspberry Pi and go to website: http://smartlight-frontend.herokuapp.com/


#### II. Motivation

We hope to create a tool that helps older people(especially those that are bothered by dementia) live a better life. Basically, we want to use various algorithms on cameras to build a smart home for older people so that they can be in a safer and more protected environment. The main part of the project includes using machine learning algorithms and object detection algorithms on cameras to detect where the older person is located and trigger related functions such as turn on or dimmer the light. Besides, we also want to detect long-time static movement of the elder person in places where they are not supposed to spend a lot of time. In that case, we send an alarm to the caregiver because that means the older person may be in danger such as slipped.

#### III. Storyboard
![storyboard](https://user-images.githubusercontent.com/89815599/145871969-4a55d868-106b-4d88-a402-364dc368e0cb.jpg)

#### IV. Timeline
11/23 - 11/28	Design and Prototype the device 
<br>	11/29 - 12/03	Build the device and Test the functionality
<br>	12/04 - 12/05	Improve the device & UI design
<br>	12/06 - 12/07	Make the video and wrap-up the documentation 

#### III. Parts Needed

Web Camera, Microphone, speaker, phone for lighting source, distance sensor

#### IV.  Risks/Contingencies

One difficulty on the technical side is that the object detection part of the project won’t work and we are not able to successfully locate the person in the scene. Besides, we need to find an efficient way to teach machine learning models to know what people fall look like.

And another major difficulty is that we have planned many functions and therefore we may not have time to finish all of them.
 
#### V.   Development & Design

Our project requires detecting long-time static movement of the elder people and giving alerts to the caregivers. After receiving the alert, the caregivers make decisions to take care of the elder people by themselves or ask for help. Eventually, the elder people will be notified by caregivers’ decisions and will shortly receive the care they need.  
*Object Detection*

We experimented with several different object detection algorithms. Eventually we chose to use sample codes from CV Zone. This sample code utilizes a pre pre-trained neural network that could identify more than 90 classes of objects. In order to cater our needs, we expand the default object detection area so that small objects will not be detected in the frame and we can focus on big objects such as human beings.  

*Alert Algorithm*

As our object detection algorithm only labeled the objects but did not track them, we needed to find a way to track people that were detected in the frame and gave alerts if people fell on the ground. We realized that if elder people fell on the ground and they would be likely not to move, this was when we needed to alert caregivers and caregivers could take care of the elder people. Based on this idea, we first classified people that were not moving by a certain amount of distance as the same person and then if the distance traveled by the same person did not differ by a certain distance threshold within a certain time threshold, we would identify that person as fallen and alert care provider to look after elder people.

*Distance Detection in Object Recognition*

Distance detection was calculated using coordinates of the pixels by euclidean distance method. 

*Voice Interaction*

Once caregivers receive the notification, they will have two choices. If they are available at that time, they take care of elder people by themselves. If not, they may call the police or ambulance for help. In order to notify elder people with their caregivers’ choices, once caregivers make their decision, we use a voice system to tell elder people their caregivers’ decisions. We reuse the existing codes in Lab3. Although the code in Lab3 was command line, the OS package in python allows us to execute command line commands in python code. 

*MQTT*

MQTT plays an important role in our project. We used MQTT to transfer alerts and notifications between elder people and caregivers. On the elder people’s side, the raspberry pi listened to the ‘response’ topic in the broker to receive caregiver’s notification. On the caregivers’ side, the raspberry constantly listened to the ‘detect’ topic. 

*Lighting System*

We developed a lighting system that changes light intensity and the type of light based on the distance between the man’s distance to a specific object. One example usage of the system is to have smart lights for older people that change colors when they read at their table, walk in the room, and turn off after they go to sleep for a while. We used the distance sensor to check the person’s distance with the object(such as desk). When the person walks close to the desk and remains for a certain amount of time and the light is still not lit, the system automatically lights the white reading light for the man. Then when the man walks away, the light dims itself and changes the color to a more comfortable orange warm color.

Here, the light is represented by the phone. We first attempted to build the whole website using Flask front-to-end. However, after the website was uploaded to heroku, we found that there is no way to receive the MQTT message.Therefore, we finally made the light by building a website using react.js and Flask on the backend. We also used a simple dataset PostgreSQL. And we hosted all frontend, backend, and SQL on Heroku. 


#### VI. Future Development

In the future, we would like to build a smart home system with more functions and functions that are more user-friendly if we have more time. For example, we do not have enough time to build the security system and the smart medicine reminder that we hoped to build. While developing the system, falling detection was not always accurate because it can not understand the actual human gesture which gives important hints to what the person may be doing, and therefore we also hope to build a model that can identify human gestures so that we can more acutely understand the status of the elder people. 

#### VII. Video Demo

1. Version 1 - Testing detection function

https://user-images.githubusercontent.com/89815599/144531681-71100bee-b643-4138-9204-172b9a64300c.mp4

2. Version 2 - Demo Setup

![Link to the Setup Video](https://youtu.be/zrw_UAdV-2E)

3. Version 3 - Demo Video
! [Demo Video](https://www.youtube.com/watch?v=GfJMESiYbQo)

#### VIII. Appendix

1. Github link to light-frontend: https://github.com/JennyLi623/sl-frontend
2. Github link to light-backend: https://github.com/JennyLi623/smartlight
 


