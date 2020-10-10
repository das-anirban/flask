import os
# This 2 line has to be done when implementing/testing oauth locally
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

blueprint = make_google_blueprint(client_id='454404908052-8p0c2eo9jd5ucam6qtu2p97l6lnu9v8a.apps.googleusercontent.com', 
								client_secret='N5hSuTqxhoqG5aXuYSh753D4',offline=True, scope=['profile','email'])

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	if not google.authorized:
		return redirect(url_for('index'))

	return render_template('welcome.html')

@app.route('/login/google')
def login():
	if not google.authorized:
		return render_template(url_for('google.login'))

	resp = google.get("/oauth2/v2/userinfo")
	assert resp.ok, resp.text
	print(resp)
	email=resp.json()["email	"]

	return render_template('welcome.html', email=email)

if __name__ == '__main__':
	app.run(debug=True)
