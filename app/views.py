# Khalid Richards
# views.py
# Putting the "V" in "MVC"

#import strings
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm, EditProfileForm, CustomRegistrationForm, AddEventForm, CustomLoginForm
from models import User, Event, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

#Home Page
@app.route('/')
@app.route('/<signed_in>')
@login_required
def index(signed_in=False):
	user = g.user
	url_for('static', filename='styles/styles.css')
	return render_template('index.html')

#Profile Pages

@app.route('/profile/<user_id>')
@login_required
def profile(user_id):
	user = User.query.filter_by(_id = int(user_id)).first()
	if (user == None):
		flash('User not found')
		return redirect(url_for('notfound'))
	return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
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
		event = Event(title=form['title'], hosted_by=g.user._id, desc=form['description'], time_start=form['start_time'],
			time_end=form['end_time'], date=form['date'], capacity=form['capacity'], attending=0)
		db.session.add(event)
		db.session.commit()
		new_form = AddEventForm()
		return render_template('add_event.html', form=new_form, message="Your event has been properly added")
	else:
		return render_template('error404.html')

@app.route('/details/<event_id>')
def details(event_id):
    return render_template('index.html')

#Signup and signin pages
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method == 'GET'):
        url_for('static', filename='styles/styles.css')
        return render_template('signup.html')
    elif (request.method == 'POST'):
        #user_db.register_new_user(request.form)
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

@app.route('/signin', methods=['GET', 'POST'])
@oid.loginhandler
def signin():
	url_for('static', filename='styles/styles.css')
	url_for('static', filename='styles/bootstrap/css/bootstrap.min.css')
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	custom_form = CustomRegistrationForm()
	if (form.validate_on_submit()):
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['email'])
	return render_template('signin.html', title='Sign In', form=form, custom_form=custom_form, providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        user = User(email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		form = CustomLoginForm()
		return render_template('login.html', title='Log In', form = form)
	else:
		form = request.form
		user = User.query.filter_by(email=form['email'], password=form['pwd']).first()
		if user is None:
			error_msg = "Sorry, the login credentials are incorrect. Please try again."
			return render_template('login.html', form=CustomLoginForm(), error_msg=error_msg)
		login_user(user, remember = form['remember_me'])
		return redirect('index.html', username = user.fname)

@app.route('/signout')
def signout():
	logout_user()
	return redirect(url_for('index'))