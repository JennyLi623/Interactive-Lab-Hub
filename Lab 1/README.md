
# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

**Setting: The interaction happens when the person drinks water in an indoor environment. It can be anytime anywhere but especially when the user needs to work and concentrate for a long time.**
**Players: Only the user is involved in the situation. However, there should not be anyone to press the buttons randomly. **

**Activity: The user puts a cup of water on the smart cup mat. Then the cup mat tracks the user's water intake by tracking the weight change of the cup. When it is time for the user to drink water, it gleams to notify the user. The user can click a button to postpone the reminder, yet if it takes too long before the user to drink water, the color is going to change from green to red.**

**Goals: The goal of the user is to concentrate on work while remain hydrated. The goal of the smart cup mat is to remind the user to drink water**

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

![alt text](https://github.com/JennyLi623/Interactive-Lab-Hub/blob/Fall2021/storyboard.jpg)

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.

**They think that overall it is a great idea. However, one issue is that the person may not carry the mat with the person wherever he goes. However, using a cup mat allows the person to measure the water intake with different cups.**


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**I think the idea of smart cup is great. It seems can help people develop a good habit of drinking water on time. Also there is a button to snooze the light in case the user cannot drink water for some reasons. And the color changing from yellow to red indicates the urgency degree, which is intuitive. My only concern is that wether the mat can be designed to be portable enough. Since people may want to use it at many places. -- Tianyun Zou (tz392)**

**The “smart water bottle” design is a great way to systematically remind and encourage user to stay hydrated, and it allows user to focus on what they are doing by having to worry less. One nice part about the design is the (potential) ease of implementation using simple combination of digital scale and LED light. One potential problem, though, is that, depending on user preference, it may actually increase the level of distraction if the user prefers extreme focus. The snooze button sees this problem and partially addresses it, and perhaps the ability to switch the alert light on and off will be even nicer. -- Qianzhi Xu**

**Based on this discovery, I am going to add a button to the cup mat that allows it to reset the weight of the water and discard the previous weight instead of counting the weight as already drunk.**


## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

**I think generally the inkerbelle is very nice. However, it may be better if the users can pick a few colors and click if directly get the color they want. Like when people use the painting tool on the computer. They don't always need to go through a complicated tool to pick the color they want but can do so quickly with a few shortcuts.**


## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

[This is the link to the original setup](https://drive.google.com/file/d/130O3i_uyn8ptVmi-d3BP9cdIt6UOXS3s/view?usp=sharing)

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

[This is the link to the improved setup](https://drive.google.com/file/d/1TAGEkVNQqAJLUtATZWtWnf8xIfBNhLXD/view?usp=sharing)


## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

![alt text](https://github.com/JennyLi623/Interactive-Lab-Hub/blob/Fall2021/prototype.jpg)

**It should be able to be carried with the user, and therefore it should be portable and light in weight. It should be able to work with most sizes of the cups and therefore it should not be too small. It works with the cups, so it needs to be water-proof.**


## Part F. Record

[This is the link to the demo](https://drive.google.com/file/d/1t3wJFWo09HcAyW7GTecJHk08pYMMbCiB/view?usp=sharing)

**Qianzhi Xu helped me with recording the video by helping with controlling the light remotely.**
**Qianzhi Xu and Tianyun Zou helped me to give feedback to my design**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 



# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*
**I think my partners basically think the design is very good, and they like the portability and the "mute" function of the design. Besides, two suggestion they gave are demonstrate the "reset" function more clearly and let the users set a personalized timer for how long they want the device to be muted. **

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*
## Part A. Plan 

**Setting: The interaction happens when the person drinks water in an indoor environment. It can be anytime anywhere but especially when the user needs to work and concentrate for a long time.**
**Players: Only the user is involved in the situation. However, there should not be anyone to press the buttons randomly. **

**Activity: The user puts a cup of water on the smart cup mat. Then the cup mat tracks the user's water intake by tracking the weight change of the cup. When it is time for the user to drink water, it gleams to notify the user. The user can click a button to postpone the reminder, yet if it takes too long before the user to drink water, the color is going to change from green to red.**

***Improvement in Activity: The user can set reminder timer by adjusting the bar on the side of the cup mat that indicates the time to remind the user to drink water after the user uses "SNOOZE" to pause the cup mat from reminding.***

**Goals: The goal of the user is to concentrate on work while remain hydrated. The goal of the smart cup mat is to remind the user to drink water.**

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

![alt text](https://github.com/JennyLi623/Interactive-Lab-Hub/blob/Fall2021/storyboard2.jpg)

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Currently I think the interaction worked quite well, it is just the design may be improved so that it looks nicer.**


## Part C. Prototype the device
**Already set up in Part I**

## Part D. Wizard the device

**This is the improved setup, I added the timer function**

https://user-images.githubusercontent.com/89815599/133190426-63111d99-5ce4-46cf-a2b5-d59a5a1e5813.mp4



## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

![alt text](https://github.com/JennyLi623/Interactive-Lab-Hub/blob/Fall2021/prototype2.jpg)

**It should be able to be carried with the user, and therefore it should be portable and light in weight. It should be able to work with most sizes of the cups and therefore it should not be too small. It works with the cups, so it needs to be water-proof. It should contain a interface that allows user to set timer that they want to remind the user to drink water.**


## Part F. Record

**There are two updated functions of the design
1)The side bar to adjust the remind timer
2)The reset button that allows the user to change a cup of water without letting the system count the water as drank by the user.

[This is the link to the demo](https://drive.google.com/file/d/1AWObFtM7UwXUzY2eE6nt9Ku8Q-hKDF4y/view?usp=sharing)

**Qianzhi Xu helped me with recording the video by helping with controlling the light remotely.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 
