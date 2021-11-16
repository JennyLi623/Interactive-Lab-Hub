import paho.mqtt.client as mqtt
import uuid
import os


topic = 'IDD/#'

def on_connect(client, userdata, flags, rc):
    print(f"connected with reult code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    #print(f"topic: {msg, topic} msg: {msg.payload.decode('UTF-8')}")
    if msg.topic == 'IDD/detect':
        print("object stolen")   
        os.system('flite -voice st -t "Treasure Stolen! Treasure Stolen! Treasure Stolen!"')
    
client = mqtt.Client(str(uuid.uuid1()))

client.tls_set()

client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_forever()
