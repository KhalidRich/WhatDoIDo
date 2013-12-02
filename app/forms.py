from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    openid = TextField('openid')
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
	description = TextField('description', validators=[Required()])
	start_date = TextField('start_date', validators=[Required()])
	end_date = TextField('end_date', validators=[Required()])
	fb_link = TextField('fb_link', validators=[Required()])
	capacity = TextField('capacity', validators=[Required()])
	hosted_by = TextField('hosted_by', validators=[Required()])

