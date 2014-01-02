'''
Scheduling Utilities

schedule_utils.py

This helps create correct schedules for users
'''
from app import db
from app.models import User, Event, AttendanceRelation
import datetime

PREFERENCE_FIELDS = ["performing_arts", "academic", "sports", "cultural", "environmental", "arts", "gensex", "stugovt", "greek"]
PREFERENCE_FIELDS.extend(["media", "political", "religious", "service", "spinterest", "early", "midday", "late"])

def binarized_schedule_default():
	return "0"*17

def binaryize_preferences(form):
	binpref = ""
	for preference in PREFERENCE_FIELDS:
		if preference in form.keys():
			binpref += "1"
		else:
			binpref += "0"
	print len(binpref)
	return binpref

def destring_preferences(preferences):
	pref_list = []
	for p in preferences:
		pref_list.append(int(p))
	return pref_list

'''Schedule Making'''
def create_schedule(attendance_relations, attendance_recommendations):
	schedule = []
	for ar in attendance_relations:
		schedule.append(Event.query.filter_by(_id=ar.event_id).first())
	schedule = sorted(schedule, key=lambda event:event.time_start)

	for recommendation in attendance_recommendations:
		if len(schedule) > 0:
			if recommendation[0].time_start < schedule[0].time_start and recommendation[0].time_end < schedule[0].time_start:
				schedule.insert(0, recommendation[0])
			for i in xrange(len(schedule)-1):
				if recommendation[0].time_start < schedule[i].time_end and recommendation[0].time_start > schedule[i+1].time_start:
					schedule.insert(i+1, recommendation[0])
		else:
			return attendance_recommendations

	return schedule

def get_registered_events(user):
	attendance_relations = AttendanceRelation.query.filter_by(user_id=user._id)
	events = []
	for relation in attendance_relations:
		event = Event.query.filter_by(_id=relation.event_id).first()
		events.append(event)
	return events

'''Preference Matching
We're going to write these functions to start matching users to events.
'''
# checks to see how similar a person's interests are to another's.
def similarities_to(other_users, user):
	similiarities = {}
	for o_user in other_users:
		u,v = (destring_preferences(o_user.preferences), destring_preferences(user.preferences))
		similiarities[o_user._id]=_dot_product(u,v)
	return similiarities

def get_event_history(user):
	past_data = []
	ar_list = AttendanceRelation.query.filter_by(user_id=user)
	for ar in ar_list:
		event = Event.query.filter_by(_id=ar.event_id)
		if event.date < datetime.date.now():
			past_data.append((ar.user_id, ar.event_id))
	return past_data

def get_recommendations(user):
	other_users = User.query.filter(User._id != user._id)
	similar_users = similarities_to(other_users, user)
	events_today = Event.query.filter_by(date = datetime.date.today())
	events_with_scores = score_events(events_today, similar_users)
	return top_ten(events_with_scores)

def score_events(events_today, similar_users):
	events_with_scores = []
	for event in events_today:
		score = 0
		for user in similar_users.values():
			prev_events = get_event_history(user)
			for prev in prev_events:
				base = 0
				if event.event_type == prev.event_type:
					base += 1
				if time_range(event) == time_range(prev):
					base += 1
				score += similar_users[user] * base * (float(event.attending) / float(event.capacity))
		events_with_scores.append((event, score))
	return events_with_scores

def top_ten(events_with_scores):
	top_scores = sorted(events_with_scores, key=lambda event:event[1])[:10] #gets the top ten items
	return top_scores

def combine_event_list(recommendations, registered_events):
	if len(registered_events) >= 10:
		return registered_events #only recommend + register for 10 events

	#stuff

def _dot_product(u,v):
	dp = 0
	for i in xrange(min(len(u), len(v))):
		print len(u)
		print len(v)
		dp += u[i] * v[i]
	return dp