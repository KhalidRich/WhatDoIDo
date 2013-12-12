'''
Scheduling Utilities

schedule_utils.py

This helps create correct schedules for users
'''
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