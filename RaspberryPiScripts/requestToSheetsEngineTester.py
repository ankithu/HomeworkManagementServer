import sheetsEngine
def getAlarmList():
	alarmList = []
	alarms = sheetsEngine.getSheetRequest('Alarms')
	for alarm in alarms:
		if len(alarm) != 2 or alarm[0]=='Alarm':
			continue
		item = {"time":alarm[1], "message":alarm[0]}
		alarmList.append(item)
	return alarmList

def getAssignmentList():
	homeworkList = []
	assignments = sheetsEngine.getSheetRequest('Assign')
	for assignment in assignments:
		if len(assignment) != 3 or assignment[0]=='Class':
			continue
		item = {"class":assignment[0], "assignment":assignment[1], "due":assignment[2]}
		homeworkList.append(item)
	return homeworkList
