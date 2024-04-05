import json
import pyads

client_id = 15
location_id=7
zone_id=11
zone_name=''

#controller_net_id="192.168.20.50.1.1"
controller_port = 851 # use 801 for tc2, use 851 for tc3
plc_val_prefix = '.' # use . for tc2, use .GVL for tc3

mqtt_broker_details = {
    'server_url' : 'mqtt://fortuitous-optician.cloudmqtt.com',
    'user' : 'geopcxoy',
    'pass' : 'osn07Rx4Eu-C',
    'port' : 1883,
    'ssl_port' : 8883,
    'websockets_port' : 443
}


email_details = {
    'url' : 'https://l94nyfvaf3.execute-api.ap-south-1.amazonaws.com/v1/device_update_status',
    'username' : 'quantum_email_alerts_username',
    'password' : 'pwd_email_alerts_user'
}

parameter_list = {
        "device_type" : "CoSensor",
        "mqtt_topic" : "quantumCoSensors_ruturaj",
        "table" : "dummy_ruturaj",
        "frequency" : 36000,
        "counter" : 0,
        "controllers" : [
            {
                "controller_name": "lbController",
                "controller_net_id": '192.168.20.50.1.1',
                "controllerObj": None,
                "items" : [
                    {
                        "id" : "UBCoSensor1Value",
                        "name" : "Upper Basement Co Sensor 1 Value",
                        "dbWrite" : True,
                        "parameters" : [
                            {
                                "PLCVariableName" : "UBCoSensor1Value",
                                "PLCVariableDataType" : pyads.PLCTYPE_INT,
                                "MQTTVariableName" : "UBCoSensor1Value",
                                "columnName": "sensor_value",
                                "lastValue" : 0,
                                "dbWrite":True,
                                "default_value":23
                            }
                        ]
                    },
                ]
            },
            {
                "controller_name": "lb2Controller",
                "controller_net_id": '192.168.20.60.1.1',
                "items" : [
                    {
                        "id" : "LBCoSensor1Value",
                        "name" : "Lower Basement Co Sensor 1 Value",
                        "dbWrite" : True,
                        "parameters" : [
                            {
                                "PLCVariableName" : "LBCoSensor1Value",
                                "PLCVariableDataType" : pyads.PLCTYPE_INT,
                                "MQTTVariableName" : "LBCoSensor1Value",
                                "columnName": "sensor_value",
                                "lastValue" : 0,
                                "dbWrite":True,
                                "default_value":24
                            }
                        ]
                    }
                ]
            }
        ]
}