# Khalid Richards
# whatdoido.py
# Routes for the app


from flask import Flask 
app = Flask(__name__)

#Home Page
@app.route('/')
def index(name=None):
	return render_template('index.html', name=name)

#Profile page
@app.route('/profile')
def profile():
	return "This is the user profile page"

#Add Events page
@app.route('/add')
def add():
	return "This is the event add page"

@app.route('/details/<event_id>')
def details(event_id):
	return "This is the details page for event # %s" % event_id