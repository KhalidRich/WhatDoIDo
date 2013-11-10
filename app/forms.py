from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditProfileForm(Form):
	email = TextField('email', validators = [Required()])
	fname = TextField('fname', validators = [Required(), Length(max=120)])
	lname = TextField('lname', validators = [Required(), Length(max=25)])
	school = TextField('school', validators = [Required(), Length(max=25)])
	sex = TextField('sex', validators = [Required()])



