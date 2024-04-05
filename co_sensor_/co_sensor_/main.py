from xmlrpc.client import TRANSPORT_ERROR
import threading
import json
from datetime import datetime
import time
import sys
import os

# Importing local modules
import gvl
import plc
import mqtt_service as mqtt
import telegram_send_message
import database as db
import pyads

# Adding telegram module path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'telegram'))

web_send_counter = 300,
web_send_threshold = 300
dbWritten = False

# Global variables for database write tracking
dbLastWriteYear = None
dbLastWriteMonth = None
dbLastWriteDay = None
dbLastWriteHour = None
dbLastWriteMinute = None

def data_retrieval_repeater():
    """
    Function to continuously retrieve data from PLC and publish it via MQTT.
    """
    global dbLastWriteYear, dbLastWriteMonth, dbLastWriteDay, dbLastWriteHour, dbLastWriteMinute, web_send_counter, web_send_threshold 


    while True:
        dt = datetime.now()
        
        complete_database_set = []
        field_list = []
        value_list = []

        mqtt_obj = {"device_type" : gvl.parameter_list["device_type"],"items" : []}

        for controller in gvl.parameter_list["controllers"]:
            #plcObj = pyads.Connection(controller["controller_net_id"], port=gvl.controller_port)
            #plcObj.open()
            
            for item in controller['items']:
                item_table_data = {"co_sensor_id": item["id"], "co_sensor_name": item["name"]}
                
                
                mqtt_item_data = {"item_id" : item["id"],"item_name" : item["name"],"parameters" : []}
                
                for param in item["parameters"]:
                    try:
                        x = param["default_value"]
                        #x = plcObj.read_by_name("GVL."+param["PLCVariableName"], param["PLCVariableDataType"])
                        # print("x:", x) 
                        parameter_data = {param["MQTTVariableName"] : x}
                        mqtt_item_data["parameters"].append(parameter_data) 
                    
                        if item["dbWrite"] and param["dbWrite"] and "columnName" in param:
                            item_table_data[param.get("columnName")] = x
                            field_list.append(param.get("columnName"))
                            value_list.append(x)
                            
                        
                    except pyads.ADSError:
                        print(f"unable to find PLC variable GVL{gvl.plc_val_prefix}{param['PLCVariableName']}")

                mqtt_obj["items"].append(mqtt_item_data)


                if item.get("dbWrite"):
                    complete_database_set.append(item_table_data)
 
                
        print("---------------------")  
        print(mqtt_obj)
        print("-----------------------")
        mqtt.publish(gvl.parameter_list['mqtt_topic'], json.dumps(mqtt_obj))
        
        

        if complete_database_set:
            if dbLastWriteYear != dt.year or dbLastWriteMonth != dt.month or dbLastWriteDay != dt.day or dbLastWriteHour != dt.hour:
                for sensor in complete_database_set:
                    table_name = "dummy_ruturaj"
                    #fields = sensor.keys()
                    fields = ['co_sensor_id','co_sensor_name','co_sensor_value']
                    values = sensor.values()
                    db.insert_record(table_name, fields, values)
                dbLastWriteYear = dt.year
                dbLastWriteMonth = dt.month
                dbLastWriteDay = dt.day
                dbLastWriteHour = dt.hour
                dbLastWriteMinute = dt.minute
                
        # print("Field List:", field_list)
        # print("Value List:", value_list)
        
        
        
        time.sleep(2)



# Initializing PLC connection and MQTT connection
plc.check_controller_availability(gvl.parameter_list)



mqtt.connect()
#mqtt.handle_message(gvl.parameter_list["mqtt_topic"],message="Meg")

#print(gvl.mqttc.on_message)
#print(gvl.on_connect())

# Starting data retrieval thread
data_retrieval_repeater()
input("")        
    
