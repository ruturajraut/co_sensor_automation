import mysql.connector
from datetime import datetime
import gvl

print ("database connected")





'''def insert_pump_record(data):
    # print("----------------------------------------------")
    print(data)
    # print("-----------------------------------------------")
    # return
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO quantum_water_pumps (pump_id,pump_name,run_status,auto_manual,temperature,dt)"
      sql = sql +" VALUES (%s,%s,%s,%s,%s,%s)"
      temperature = None
      
      if("temperature" in data):
        temperature = data["temperature"]

      val = (data["pump_id"],data["pump_name"],data["run_status"],data["auto_manual"],temperature,timestamp)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      mycursor.close()
      mydb = None
      return True
    except:
      print("Error while inserting data to the database")'''
print("===============")
def insert_record(table_name, fields, values):
    print("Inside function ----------")
    
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      
      '''field_names = ', '.join(fields)
      value_placeholders = ', '.join(['%s'] * len(values))
      sql = f"INSERT INTO {table_name}({field_names}, dt) VALUES ({value_placeholders}, %s)"
      
      sql = "INSERT INTO quantum_co_sensors(sensor_id,sensor_name,sensor_value,dt)"
      sql = sql +" VALUES (%s,%s,%s,%s)"
      val = (data["sensor_id"],data["sensor_name"],data["sensor_value"],timestamp)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "co sensor record inserted.")
      mycursor.close()
      mydb = None
      return True
    except:
      print("Error while inserting co sensor data to the database")'''
      
      # Constructing the SQL query dynamically
      field_names = ', '.join(fields)  # Joining field names with comma
      value_placeholders = ', '.join(['%s'] * len(values))  # Generating placeholders for values
      sql = f"INSERT INTO {table_name}({field_names}, dt) VALUES ({value_placeholders}, %s)"  # Creating the SQL query
      val = tuple(values) + (timestamp,)  # Combining values with timestamp
      
      print("--------------999",val)

      # Execute the SQL query
      mycursor.execute(sql, val)

      # Commit the transaction
      mydb.commit()

      # Print the number of records inserted
      print(mycursor.rowcount, "record inserted.")

      # Close cursor
      mycursor.close()

      # Close database connection
      mydb.close()

      return True  # Return True indicating success
    except Exception as e:
        # If an error occurs, print the error message
        print("Error:", e)
        print("Error while inserting data to the database")
        return False  # Return False indicating failure

# Example usage:
#table_name = "dummy_ruturaj"
#fields = ["co_sensor_id", "co_sensor_name", "co_sensor_value"]
#values = [213, "sensor1", 5.6]

#insert_record(table_name, fields, values)


def insert_alert(type, msg):
  # print("----------------------------------------------")
    print(type,msg)
    # print("-----------------------------------------------")
    # return

    '''msg = data["pump_name"] + " -  Status : "
    if(data["run_status"]):
      msg += "ON"
    else:
      msg += "OFF"

    msg += " | Mode : "

    if(data["auto_manual"]):
      msg += "AUTO"
    else:
      msg += "MANUAL"

'''
    try:
      mydb = mysql.connector.connect(
        host="claypot-db-instance.ci3ywfy1btrn.ap-south-1.rds.amazonaws.com",
        user="claypot_db_user",
        password="claypot_db_user_password",
        database="claypot_db"
      )

      mycursor = mydb.cursor()

      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      sql = "INSERT INTO quantum_alerts (dt,type,message,ack)"
      sql = sql +" VALUES (%s,%s,%s,%s)"
      val = (timestamp,3,msg,0)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "alert record inserted.")
      mycursor.close()
      mydb = None
      return True
    except:
      print("Error while inserting data to the alert table")