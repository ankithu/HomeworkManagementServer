#import necesary libs
import requests
import json
from datetime import datetime 
import time as t
import lightsEngine as lights
import speechEngine
import requestToSheetsEngineTester as requestToSheet
import googleCalenderEngine as calenderSpeech
#master lists for assignment and alarm storage
alarms = []
homework = []

#program states
prevSwitch = lights.getSwitch()
class State():
        WAITING = 0
        ALARM = 1
        ASSIGNMENTS = 2

state = State.WAITING
#Loop forever
while True:
        switch = lights.getSwitch()
        toggle = (switch != prevSwitch)
        if (state == State.WAITING):
                alarms = requestToSheet.getAlarmList()
                print(alarms)
                print(homework)
                now = datetime.now()
                clock = now.strftime("%H:%M")
                print(clock)
                #alarm condition met
                if any(alarm['time'] == clock for alarm in alarms) or (any(alarm['time'] == clock[1:] for alarm in alarms) and clock[0]=='0'):
                        state = State.ALARM 
                else:  
                        t.sleep(10)
        elif (state == State.ALARM):
                print("ALARM ALERT")
                speechEngine.say('WAKE UP RIGHT NOW')
                #lights.lights(True)
                if (toggle):
                        state = STATE.ASSIGNMENTS
        elif (state == State.ASSIGNMENTS):
                homework = requestToSheet.getAssignmentList()
                speechEngine.say("Good morning Ankith!")
                speechEngine.say("Here's a look at your upcoming assignments.")
                for work in homework:
                        sayString = "In " + work["class"] + " you have " + work["assignment"] + " due " + work["due"]
                        speechEngine.say(sayString)
                        calenderSpeech.sayEvents(speechEngine)
                speechEngine.say("Have a great day today Ankith!")
                state = STATE.WAITING

        prevSwitch = switch
        t.sleep(2)

