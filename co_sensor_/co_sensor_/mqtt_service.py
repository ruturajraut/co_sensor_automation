import sys
import paho.mqtt.client as mqtt
import os
import urllib.parse as urlparse
import time
import json
import gvl
import plc


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'telegram'))

try:
    import telegram_send_message
except Exception as e:
    print("Telegram Exception:")
    print(e)
    print("telegram exception ended")

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'blu'))

try:
    import blu
    print("blu app imported and connected")
except Exception as e:
    print("blu app import Exception:")
    print(e)
    print("blu app import exception ended")

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    

def on_disconnect(client, userdata, rc):
    print("disconnected...")
    connect()

def on_message(client, obj, msg):
    handle_message(msg.topic, msg.payload.decode('utf-8'))

def on_publish(client, obj, mid):
    print("Message published with MID " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

def connect():
    url_str = gvl.mqtt_broker_details["server_url"]
    print("Connecting to MQTT broker at " + url_str)
    url = urlparse.urlparse(url_str)
    mqttc.username_pw_set(gvl.mqtt_broker_details["user"], gvl.mqtt_broker_details["pass"])
    # print("Ruturaj Connect inside")
    isMqttConnected = False

    while not isMqttConnected:
        try:
            mqttc.connect(url.hostname, gvl.mqtt_broker_details["port"])
            # print("Ruturaj Connect inside 2")

            mqttc.loop_start()
            isMqttConnected = True
        except Exception as e:
            print(f"Unable to connect to MQTT: {e}")
            time.sleep(10)

def handle_message(topic, message):
    # Check if controller is available
    if plc.check_controller_availability(gvl.parameter_list):
        # Implement CO sensor message handling logic here
        print(f"Received message on topic '{topic}': {message}")
    else:
        print("Controller is not available. Cannot handle message.")
        
def subscribe(topic):
    # Start subscribe, with QoS level 0
    mqttc.subscribe(topic, 0)
    

def publish(topic,message):
    # Publish a message
    mqttc.publish(topic, message)
# Call the connect function to establish MQTT connection
connect()
