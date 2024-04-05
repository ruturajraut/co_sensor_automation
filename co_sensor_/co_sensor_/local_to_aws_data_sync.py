import mysql.connector
from datetime import datetime
import gvl
import database as local_db


def sync_records():
    try:
      aws_db = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = aws_db.cursor()

      records = local_db.get_all_records()
      print('records to be synced with server')
      print('------------------------------')

      

      for x in records:
        
        # print(x)
        record_id = x['_id']
        device_id = x['device_id']
        device_name = x['device_name']
        param_id = x['param_id']
        param_name = x['param_name']
        value = x['value']
        dt = x['dt']
        setpoint_low = x['setpoint_low']
        setpoint_high = x['setpoint_high']
        isAlarm = x['isAlarm']

        # COMMENT THIS LATER
        # device_id = 100

        # INSERTING RECORD INTO MYSQL DATABASE
        sql = "INSERT INTO server_monitoring (client_id,zone_id,device_id,device_name,param_id,param_name,value,dt,setpoint_low,setpoint_high,isAlarm)"
        sql = sql +" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (gvl.client_id,gvl.zone_id,device_id,device_name,param_id,param_name,value,dt,setpoint_low,setpoint_high,isAlarm)
        mycursor.execute(sql, val)
        aws_db.commit()
        print(mycursor.rowcount, "record inserted.")

        local_db.delete_record_by_id(record_id)

      mycursor.close()
      aws_db = None

    except mysql.connector.Error as err:
      print("Error while conencting and inserting data into AWS database")
      print(err)
      

#insert_param_record()