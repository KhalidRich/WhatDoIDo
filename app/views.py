# Khalid Richards
# views.py
# Putting the "V" in "MVC"

#import strings
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

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

#Profile page
@app.route('/profile')
def profile():
    return render_template('index.html')

#Add Events page
@app.route('/add')
def add():
    return render_template('index.html')

@app.route('/details/<event_id>')
def details(event_id):
    return render_template('index.html')

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

@app.route('/signin', methods=['GET', 'POST'])
@oid.loginhandler
def signin():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))

	form = LoginForm()
	if (form.validate_on_submit()):
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['email'])
	return render_template('signin.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

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
