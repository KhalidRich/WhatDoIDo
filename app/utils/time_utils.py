# Khalid Richards
# December 11, 2013
# time_utils.py

import datetime

MONTHS = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6,
 "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}

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
		month = MONTHS[args[0][:len(args[0]) - 4]]
		day = int(args[0][len(args[0]) - 3 : len(args[0])])
		year = int(args[1])
		return datetime.date(year, month, day)


