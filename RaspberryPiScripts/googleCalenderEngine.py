from __future__ import print_function
from datetime import datetime
from dateutil import tz
from datetime import timedelta
import dateutil.parser
est = tz.gettz('America/Detroit')
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import time as t
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def sayEvents(speechEngine):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    #today = datetime.utcnow().date()
    #start = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc()).astimezone(est)
    #end = start + timedelta(1)
    #print(start.isoformat())
    #print(end.isoformat())
    today = datetime.now().date()
    dateString = today.strftime("%Y-%m-%d")
    events_result = service.events().list(calendarId='primary', timeMin=dateString+'T00:00:00-00:00',
                                        maxResults=10, timeMax= dateString+'T23:59:00-00:00',singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    sayString = 'Today you have the following events: '
    sayList = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        #speechEngine.say(str(start)+str(event['summary']))
        sayList.append(str(event['summary']))
        print(start, event['summary'])
    speechEngine.say(sayString)
    t.sleep(0.5)
    speechEngine.say(sayList[0])
    t.sleep(1.0)
    for event in sayList[1:]:
        speechEngine.say('and ' + event)
        t.sleep(1.0)
