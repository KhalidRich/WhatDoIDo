'''
string_utils.py
Helper functions for strings and stuff
'''

REGISTRATION_SUCCESS = "Congrats! You successfully registered for this event!"

EVENT_ADD_SUCCESS = "Congrats! You sucessfully added your first event!"

EVENT_TYPES = [("Performing Arts", "Performing Arts"), ("Academic", "Academic"), ("Cultural", "Cultural"), ("Environmental",
	"Environmental"), ("Visual Arts", "Visual Arts"), ("Gender and Sexuality", "Gender and Sexuality"), ("Student Government",
	"Student Government"), ("Greek", "Greek"), ("Media and Publications", "Media and Publications"), ("Political", 
	"Political"), ("Religious/Spiritual", "Religious/Spiritual"), ("Service", "Service"), ("Special Interest", "Special Interest")]

def cint(strint):
	return int(strint.replace(',', ''))