# Khalid Richards
# models.py
# A list of models for the app 

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

SEX_MALE = 0
SEX_FEMALE = 1

class User(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	fname = db.Column(db.String(25))
	lname = db.Column(db.String(25))
	school = db.Column(db.String(25))
	sex = db.Column(db.SmallInteger)
	role = db.Column(db.SmallInteger, default=ROLE_USER)

	def get_id(self):
		return unicode(self._id)

	def is_authenticated(self):
		return True

	def is_anonymous(self):
		return False

	def is_active(self):
		return True

class Event(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(150))
	hosted_by = db.Column(db.Integer, db.ForeignKey('user._id'))
	desc = db.Column(db.String(2000))
	time_start = db.Column(db.String(5))
	time_end = db.Column(db.String(5))
	date = db.Column(db.String(11))

# User
