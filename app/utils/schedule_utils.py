'''
Scheduling Utilities

schedule_utils.py

This helps create correct schedules for users
'''

PREFERENCE_FIELDS = ["performing_arts", "academic", "sports", "cultural", "environmental", "arts", "gensex", "stugovt", "greek"]
PREFERENCE_FIELDS.extend(["media", "political", "religious", "service", "spinterest", "early", "late", "midday"])

def create_schedule(events):
	schedule = []
	while(True):
		next_event = None
		if len(schedule) == 0:
			event = search_first_event(events)
			schedule.append(event)
		else:
			for event in events:
				if event.time_start > schedule[len(schedule) - 1].time_end:
					next_event = event
		if next_event is None:
			return schedule

def binarized_schedule_default():
	return "0"*15

def binaryize_preferences(form):
	binpref = ""
	for preference in PREFERENCE_FIELDS:
		if preference in form.keys():
			binpref += "1"
		else:
			binpref += "0"
	return binpref