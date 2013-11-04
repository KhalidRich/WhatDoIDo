# Khalid Richards
# whatdoido.py
# Routes for the app


from flask import Flask, render_template, url_for
app = Flask(__name__)

#Home Page
@app.route('/')
def index():
	url_for('static', filename='styles/styles.css')
	return render_template('index.html')

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

if(__name__ == "__main__"):
	app.run(debug=True)
