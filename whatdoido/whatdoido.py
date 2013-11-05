# Khalid Richards
# whatdoido.py
# Routes for the app


from flask import Flask, render_template, url_for, request
app = Flask(__name__)

#Home Page
@app.route('/')
@app.route('/<signed_in>')
def index(signed_in=False):
    url_for('static', filename='styles/styles.css')
    return render_template('index.html', signed_in=False)

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
    elif request.method == 'POST':
        #derp
        return render_template('error404.html')
    else:
        return render_template('error404.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if(request.method == 'POST'):
        return render_template('signed_in.html')
        #sign_in()
    elif request.method == 'GET':
        url_for('static', filename='styles/styles.css')
        return render_template('signin.html')
    else:
        return render_template('error404.html')

if(__name__ == "__main__"):
    app.run(debug=True)
