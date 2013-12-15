from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, Length

import utils.string_utils as string_utils

class LoginForm(Form):
    openid = TextField('openid')
    remember_me = BooleanField('remember_me', default = False)

class CustomLoginForm(Form):
	email = TextField('email', validators = [Required()])
	password = TextField('password', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class CustomRegistrationForm(Form):
	email = TextField('email', validators = [Required()])
	fname = TextField('fname', validators = [Required(), Length(max=120)])
	lname = TextField('lname', validators = [Required(), Length(max=25)])
	school = TextField('school', validators = [Required(), Length(max=25)])
	sex = TextField('sex', validators = [Required()])
	password = TextField('sex', validators = [Required()])

class EditProfileForm(Form):
	email = TextField('email', validators = [Required()])
	fname = TextField('fname', validators = [Required(), Length(max=120)])
	lname = TextField('lname', validators = [Required(), Length(max=25)])
	school = TextField('school', validators = [Required(), Length(max=25)])
	sex = TextField('sex', validators = [Required()])

class AddEventForm(Form):
	title = TextField('title', validators = [Required()])
	description = TextAreaField('description', validators=[Required()])
	date = TextField('date', validators=[Required()])
	start_time = TextField('start_time', validators=[Required()])
	end_time = TextField('end_time', validators=[Required()])
	fb_link = TextField('fb_link', validators=[Required()])
	capacity = TextField('capacity', validators=[Required()])
	hosted_by = TextField('hosted_by', validators=[Required()])
	event_type = SelectField('event_type', choices=string_utils.EVENT_TYPES, validators=[Required()])

class UserPreferenceForm(Form):
	performing_arts = BooleanField('performing_arts')
	academic = BooleanField('academic')
	sports = BooleanField('sports')
	cultural = BooleanField('cultural')
	environmental = BooleanField('environmental')
	arts = BooleanField('arts')
	gensex = BooleanField('gensex')
	stugovt = BooleanField('stugovt')
	greek = BooleanField('greek')
	media = BooleanField('media')
	political = BooleanField('political')
	religious = BooleanField('religious')
	service = BooleanField('service')
	spinterest = BooleanField('spinterest')
	early = BooleanField('early')
	late = BooleanField('late')
	midday = BooleanField('midday')