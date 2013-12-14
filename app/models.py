# Khalid Richards
# models.py
# A list of models for the app 

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

SEX_MALE = 0
SEX_FEMALE = 1

IRRELEVANT = 0
RELEVANT = 1

class User(db.Model):
	_id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), unique = True)
	fname = db.Column(db.String(25))
	lname = db.Column(db.String(25))
	school = db.Column(db.String(25))
	sex = db.Column(db.SmallInteger)
	role = db.Column(db.SmallInteger, default=ROLE_USER)
	password = db.Column(db.String(25))

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
	time_start = db.Column(db.Time)
	time_end = db.Column(db.Time)
	date = db.Column(db.Date)
	event_type = db.Column(db.String(25))
	capacity = db.Column(db.Integer)
	attending = db.Column(db.Integer)

	def get_id(self):
		return unicode(self._id)

	def get_hosted_by(self):
		return unicode(self.hosted_by)

	def is_available_for_registration(self):
		return self.capacity == self.attending

	def add_registered_user(self):
		self.attending += 1

	def delete_registered_user(self):
		if self.attending > 0:
			self.attending -= 1

	def edit_capacity(self, cap):
		self.capacity = cap

	def get_event_type(self):
		return self.event_type

class AttendanceRelation(db.Model):
	event_id = db.Column(db.Integer, db.ForeignKey('event._id'), primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user._id'), primary_key=True)
	attending = db.Column(db.Integer)
	relevant = db.Column(db.Integer)

	def is_attending(self):
		return self.attending

	def is_relevant(self):
		return self.relevant