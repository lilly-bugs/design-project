#comment
import mysql.connector
import client
import time
import re
import string

mydb = mysql.connector.connect(
  host="localhost",
  user="Team5",
  password="Votion2022",
  database="test_database3"
)

mycursor = mydb.cursor(buffered=True)

def get_foodname(sensorNum):
    select_query = "SELECT foodName FROM sensorAssignments WHERE sensorNum = '%s' order by dateTime DESC LIMIT 1" %(sensorNum)
    mycursor.execute(select_query)
    foodName = mycursor.fetchone()
    return foodName

foodSensor0 = get_foodname(0)
foodSensor1 = get_foodname(1)
foodSensor2 = get_foodname(2)

def to_string(foodName):
    foodName = str(foodName)
    allow = string.ascii_letters + string.digits + ' '
    input = re.sub('[^%s]' % allow, '', foodName)
    return input

foodSensor0 = to_string(foodSensor0)
foodSensor1 = to_string(foodSensor1)
foodSensor2 = to_string(foodSensor2)
   
#host1 = '192.168.0.100'
tempSensor0 = client.return_temp('192.168.0.100')
tempSensor1 = client.return_temp('192.168.0.103')
tempSensor2 = client.return_temp('192.168.0.110')

def write_data(sensorNum, temp, foodName):
    dateWrite = time.strftime("%Y-%m-%d")
    timeWrite = time.strftime("%H:%M:%S")
    
    sql = "INSERT INTO sensor%s(foodname, temperature, time, date) VALUES (%s, %s, %s, %s)"
    val = (sensorNum, foodName, temp, timeWrite, dateWrite)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
write_data(0, tempSensor0, foodSensor0)
write_data(1, tempSensor1, foodSensor1)
write_data(2, tempSensor2, foodSensor2)