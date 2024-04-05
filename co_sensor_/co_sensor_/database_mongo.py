import pymongo
import datetime


def insert_param_record(device_id,device_name,param_id,param_name,value,setpoint_low,setpoint_high,isAlarm):
    print('inserting record to local DB')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["octopus"]
    mycol = mydb["octopus-server-room-monitoring-log"]

    dt = datetime.datetime.now()
    dt = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + " " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
    mydict = {"device_id" : device_id,"device_name" : device_name, "param_id" : param_id,"param_name" : param_name,"value" : value,"dt" : dt,"setpoint_low" : setpoint_low,"setpoint_high" : setpoint_high,"isAlarm" : isAlarm}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    

def get_all_records():
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["octopus"]
  mycol = mydb["octopus-server-room-monitoring-log"]
  return mycol.find()

def delete_record_by_id(record_id):
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["octopus"]
  mycol = mydb["octopus-server-room-monitoring-log"]
  myquery = { "_id": record_id }
  mycol.delete_one(myquery)
  print('local record deleted._id:' + str(record_id))


