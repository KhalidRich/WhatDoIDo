# Khalid Richards
# views.py
# Putting the "V" in "MVC"

#import strings
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm, EditProfileForm, CustomRegistrationForm, AddEventForm, CustomLoginForm
from models import User, Event, AttendanceRelation, ROLE_USER, ROLE_ADMIN

from utils import time_utils, string_utils

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

#Home Page
@app.route('/')
@app.route('/<signed_in>')
def index(signed_in=False):
	url_for('static', filename="styles/styles.css")
	url_for('static', filename="styles/bootstrap/css/bootstrap.min.css")
	user = g.user
	url_for('static', filename='styles/styles.css')
	user_events = []
	user_created_events = []
	if hasattr(user, '_id'):
		attendance_relations = AttendanceRelation.query.filter_by(user_id = user._id)

		for relation in attendance_relations:
			event = Event.query.filter_by(_id=relation.event_id).first()
			if time_utils.is_an_event_today(event):
				user_events.append(Event.query.filter_by(_id = event._id).first())
 
		created_events = Event.query.filter_by(hosted_by=user._id)
		for event in created_events:
			if time_utils.is_an_event_today(event):
				user_created_events.append(event)
	else:
		return render_template('home.html')
	return render_template('index.html', user_events=user_events, user_created_events=user_created_events)

#Profile Pages

@app.route('/profile/<user_id>')
def profile(user_id):
	user = User.query.filter_by(_id = int(user_id)).first()
	if (user == None):
		flash('User not found')
		return redirect(url_for('notfound'))
	return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
	form = EditProfileForm()
	if(form.validate_on_submit()):
		g.user.email = form.email.data
		g.user.fname = form.fname.data
		g.user.lname = form.lname.data
		g.user.school = form.school.data
		g.user.sex = form.sex.data
		db.session.add(g.user)
		db.session.commit()
		flash('Your changes have been saved')
		return redirect(url_for('edit_profile'))
	else:
		form.email.data = g.user.email
		form.fname.data = g.user.fname
		form.lname.data = g.user.lname
		form.school.data = g.user.school
		form.sex.data = g.user.sex
	return render_template('edit_profile.html', form=form)

#Add Events page
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
	if request.method == 'GET':
		#generate form
		form = AddEventForm()
		return render_template('add_event.html', form=form, user=g.user)
	elif request.method == 'POST':
		#add the new event; redirect to the event add form with message "Your event has been added"
		form = request.form
		event = Event(title=form['title'], _id=Event.query.count() + 1, hosted_by=g.user._id, desc=form['description'], time_start=time_utils.time_format(form['start_time']),
			time_end=time_utils.time_format(form['end_time']), date=time_utils.date_format(form['date']), capacity=string_utils.cint(form['capacity']), attending=0, event_type=form['event_type'])
		db.session.add(event)
		db.session.commit()
		new_form = AddEventForm()
		return render_template('add_event.html', form=new_form, message="Your event has been properly added")
	else:
		return render_template('error404.html')

@app.route('/details/<event_id>', methods=['GET', 'POST'])
def details(event_id):
	event = Event.query.filter_by(_id=event_id).first()

	if request.method == 'POST':
		ar = AttendanceRelation(user_id=g.user._id, event_id=event_id, attending=1, relevant=1)
		event.attending += 1
		db.session.add(ar)
		db.session.commit()
		return render_template('event_details.html', msg=string_utils.REGISTRATION_SUCCESS, event=event, ar=ar)

	ar = AttendanceRelation.query.filter_by(event_id=event_id, user_id=g.user._id).first()

	if event is None:
		return render_template('error404.html')

	if not hasattr(ar, 'event_id'):
		return render_template('event_details.html', event=event)

	else:
		return render_template('event_details.html', event=event, ar=ar)

#Signup and signin pages
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method == 'GET'):
        url_for('static', filename='styles/styles.css')
        return render_template('signup.html')
    elif (request.method == 'POST'):
        url_for('static', filename='styles/styles.css')
        return redirect('/True')
    else:
        return render_template('error404.html')

@app.route('/register', methods=['POST'])
def register():
	if session.get('signed_in'):
		redirect(url_for('index'))
	print request
	form = request.form
	if form is None:
		return render_template('error404.html')
	user = User(email=form['email'], fname=form['fname'], lname=form['lname'], school=form['school'], password=form['pwd'])
	db.session.add(user)
	db.session.commit()
	login_user(user)
	return redirect(url_for('index'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		form = CustomLoginForm()
		return render_template('login.html', title='Log In', form = form)
	else:
		form = request.form
		user = User.query.filter_by(email=form['email'], password=form['password']).first()
		if user is None:
			error_msg = "Sorry, the login credentials are incorrect. Please try again."
			return render_template('login.html', form=CustomLoginForm(), error_msg=error_msg)
		if 'remember_me' in form:
			login_user(user, remember = form['remember_me'])
		else:
			login_user(user)
		return redirect('index.html')

@app.route('/signout')
def signout():
	logout_user()
	return redirect(url_for('index'))