# Khalid Richards
# December 11, 2013
# time_utils.py

import datetime

MONTHS = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6,
 "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def time_format(stime):
	cindex = stime.find(":")
	hour = int(stime[:cindex])

	if "PM" in stime and hour != 12:
		hour += 12

	if "PM" not in stime and hour == 12:
		hour = 0

	minutes = int(stime[cindex+1:cindex+3])
	return datetime.time(hour, minutes)

def date_format(sdate):
	if 10 == len(sdate):
		args = sdate.split("/")
		return datetime.date(int(args[2]), int(args[0]), int(args[1]))
	else:
		args = sdate.split(",")
		month = MONTHS[args[0][:len(args[0]) - 3].capitalize()]
		day = int(args[0][len(args[0]) - 3 : len(args[0])])
		year = int(args[1])
		return datetime.date(year, month, day)

def get_time_dict(events):
	time_dict = {}
	for event in events:
		time_list[event._id] = event.time
	return time_dict

'''
Determines whether some event is today.
'''
def is_an_event_today(event):
	mtoday = datetime.date.today()
	mtmrw = mtoday.replace(day=mtoday.day+1)
	print event.date
	return event.date >= mtoday and event.date < mtmrw