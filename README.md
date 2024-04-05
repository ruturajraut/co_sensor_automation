# co_sensor_automation
co_sensor device automation project using PLC, Python, SQL, AWS, Html, CSS. NodeJs.

#Description:
Python script appears to be part of an industrial automation system. Let's break down the main components and functionalities.
co_sensor Automation Framework using PLC Controller and Python with the below features:

Requirements:

Python 3.x
Libraries:
          xmlrpc.client
          threading
          json
          datetime
          time
          sys
          os
          pyads (for interacting with PLCs)
          Other custom modules (gvl, plc, mqtt_service, telegram_send_message, database) specific to the project environment

Usage:

Ensure all required libraries and modules are installed.
Configure the script parameters in gvl.py, plc.py, mqtt_service.py, and other custom modules as necessary.
Run the script using Python: python data_retrieval_script.py.


Certainly! Let's break down the code step by step.

Imports
python
Copy code
from xmlrpc.client import TRANSPORT_ERROR
import threading
import json
from datetime import datetime
import time
import sys
import os
These are the necessary imports for various functionalities in the script. xmlrpc.client is used for handling XML-RPC client-server communication. threading is used for multi-threading. json is for JSON serialization and deserialization. datetime is used for working with dates and times. time is used for time-related functions. sys and os are used for system-specific parameters and functions.

Global Variables
python
Copy code
web_send_counter = 300,
web_send_threshold = 300
dbWritten = False
dbLastWriteYear = None
dbLastWriteMonth = None
dbLastWriteDay = None
dbLastWriteHour = None
dbLastWriteMinute = None
These are global variables used throughout the script to track various states and data for database writing.

Function: data_retrieval_repeater()
This function continuously retrieves data from PLC and publishes it via MQTT.

It iterates through controllers and their items defined in gvl.parameter_list.
For each item, it retrieves parameters from the PLC and prepares MQTT payloads.
If configured, it writes data to the database.
It then publishes the MQTT payload.
Finally, it sleeps for 2 seconds before repeating the process.
Initialization
python
Copy code
plc.check_controller_availability(gvl.parameter_list)
mqtt.connect()
This part initializes the PLC connection by checking the availability of controllers specified in gvl.parameter_list and connects to the MQTT broker.

Main Execution
python
Copy code
data_retrieval_repeater()
input("")
It starts the data retrieval function in a loop and waits for user input to exit. The loop runs indefinitely until the user provides input.

Explanation
The script continuously collects data from PLCs, formats it into MQTT messages, and publishes them. If specified, it also writes data to the database. The script is structured to run indefinitely until stopped by the user.

The global variables track the last write time to the database and other related states. The code seems to be part of a larger system responsible for data acquisition and possibly control in an industrial environment, integrating PLCs, MQTT for communication, and a database for storage.

Please note that some parts of the code are commented out (plcObj initialization and usage), likely for testing purposes or because they are incomplete. The functionality related to Telegram integration is imported but not directly used in the provided script.


          
