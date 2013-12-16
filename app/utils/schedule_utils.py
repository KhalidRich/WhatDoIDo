'''
Scheduling Utilities

schedule_utils.py

This helps create correct schedules for users
'''
from app import db
from models import User, Event, AttendanceRelation
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
def make_schedule(user, events):
	other_users = User.query.all()
	similiarity_index = similiarities_to(other_users, users)
	past_data, anticipation_data = past_and_future_event_data_from(other_users)
	recommendations = get_recommendations(similiarity_index, past_data, anticipation_data)
	registered_events = get_registered_events(user)
	return combine_event_list(recommendations, registered_events)

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
	similiarities = []
	for o_user in other_users:
		u,v = (destring_preferences(o_user.preferences), destring_preferences(user.preferences))
		similiarities.append((o_user._id, _dot_product(u, v)))
	return similiarities

def past_and_future_event_data_from(other_users):
	past_data = []
	anticipation_data = []
	for user in other_users:
		ar_list = AttendanceRelation.query.filter_by(user_id=user._id)
		for ar in ar_list:
			event = Event.query.filter_by(_id=ar.event_id)
			if event.date < datetime.date.now():
				past_data.append(ar.user_id, ar.event_id, (float(ar.anticipation + ar.rating) / 2.0))
			else:
				anticipation_data.append(ar.user_id, ar.event_id, float(ar.anticipation))
	return past_data

def get_recommendations(similiarity_index, past_data, anticipation_data):
	#stuff

def combine_event_list(recommendations, registered_events):
	if len(registered_events) >= 10:
		return registered_events #only recommend + register for 10 events

	#stuff

def _dot_product(u,v):
	dp = 0
	for i,v in (u,v):
		dp += u * v
	return dp