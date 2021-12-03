# Final Project
![Blue Clinical Friendly Vaccine Information General Health Poster](https://user-images.githubusercontent.com/89815599/144530504-b706848a-c3c8-42da-a48d-8aa3df0fa5b1.gif)
Team member  **Jueying Li(jl2852)** and **Shengnan Han(sh2556)**

## Project Proposal

#### I.   Big Idea

We hope to create a tool that helps older people(especially those that are bothered by dementia) live a better life. Basically, we want to use various algorithms on cameras to build a smart home for older people so that they can be in a safer and more protected environment. The main part of the project includes using machine learning algorithms and object detection algorithms on cameras to detect where the older person is located and trigger related functions such as turn on or dimmer the light. Besides, we also want to detect long-time static movement of the older person in places where they are not supposed to spend a lot of time. In that case, we send an alarm to the caregiver because that means the older person may be in danger such as slipped.

#### II.  Timeline
11/23 - 11/28	Design and Prototype the device 
<br>	11/29 - 12/03	Build the device and Test the functionality
<br>	12/04 - 12/05	Improve the device & UI design
<br>	12/06 - 12/07	Make the video and wrap-up the documentation 

#### III. Parts Needed

Web Camera, Microphone, speaker, phone for lighting source, distance sensor

#### IV.  Risks/Contingencies

One difficulty on the technical side is that the object detection part of the project won’t work and we are not able to successfully locate the person in the scene. Besides, we need to find an efficient way to teach machine learning models to know what people fall look like.

And another major difficulty is that we have planned many functions and therefore we may not have time to finish all of them.
 
#### V.    Fall-Back Plan

If we encounter the first problem, we will use other sensors to make sure that we still have most of the functionalities of the smart home accomplished. Besides, we have written down a list of functions to implement in chronological order based on their importance. And therefore, if we encounter the second problem, we will still have the most relevant functions finished.

## Design

### Part 1 How it works
Currently, the design is very straight forward. A camera is used to detect whether a person falls down and sends signal based on the detections. Meantime, the client side listens to the detection, and receive both audio and video alert if an event occured. The person that receives the mesage can push a button to stop receiving the alert. We have dedicated a lot of time currently on developing the cod to detect falling. Now that this part is done, we will expand the code to d more interesting stuff and improve the UI design.

### Part 2 Storyboard

### Techniques used

We have tried out many ways to detect the falling event. And what seems to work best is to detect the person when the person stops moving and the square becomes horizntal instead of vertical. 

## Video Demo
https://user-images.githubusercontent.com/89815599/144531681-71100bee-b643-4138-9204-172b9a64300c.mp4



