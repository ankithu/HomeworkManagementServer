#import necesary libs
import requests
import json
from datetime import datetime 
import time as t
import lightsEngine as lights

#master lists for assignment and alarm storage
alarms = []
homework = []

#Loop forever
while True:
        #make and process a request to the alarms section of the api. Parse all alarms and add it to the list if it's unique
        alarmR  = requests.get("http://homework-manage.herokuapp.com/api/alarms")
        alarmsString = alarmR.content
        alarmObjects = json.loads(alarmsString)
        #clears the list in case the user removed alarms using web interface
        alarms *= 0
        for alarmObject in alarmObjects:
                name = alarmObject["alarm"]
                time = alarmObject["time"]
                item = {"time": time, "message": name}
                #precautionary for duplicates
                if item not in alarms:
                        alarms.append(item)
        print(alarms)
        #make and process a request to the assignments section of the api. Parse all assignments and add it to the list if its unique
        assignR = requests.get("http://homework-manage.herokuapp.com/api/assignments")
        assignString = assignR.content
        assignObjects = json.loads(assignString)
        for assignObject in assignObjects:
                name = assignObject["assignment"]
                duedate = assignObject["duedate"]
                hour = assignObject["hour"]
                item = {"duedate":duedate,"hour":hour,"name":name}
                if item not in homework:
                        homework.append(item)
        print(homework)
        now = datetime.now()
        clock = now.strftime("%H:%M")
        print(clock)
        if any(alarm['time'] == clock for alarm in alarms) or (any(alarm['time'] == clock[1:] for alarm in alarms) and clock[0]=='0'):
                print("ALARM ALERT")
                lights.lights(True)
        t.sleep(1)