import os
# This 2 line has to be done when implementing/testing oauth locally
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized
from flask_login import logout_user

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
	resp = google.get("/oauth2/v1/userinfo")
	assert resp.ok, resp.text
	email=resp.json()["email"]
	name=resp.json()["name"]
	#print(resp)
	return render_template("welcome.html",email=name)

@app.route('/login/google')
def login():
	#print (google.authorized)
	if not google.authorized:
		return redirect_to(url_for('google.login'))

	resp = google.get("/oauth2/v1/userinfo")
	assert resp.ok, resp.text
	email=resp.json()["email"]
	
	return render_template("welcome.html",email=email)

@oauth_authorized.connect
def redirect_to_next_url(blueprint, token):
	print(token)
	blueprint.token = token
	next_url = url_for('welcome')
	return redirect(next_url)

@app.route("/logout")
def logout():
	if google.authorized:
	    token = blueprint.token["access_token"]
	    resp = google.post(
	        "https://accounts.google.com/o/oauth2/revoke",
	        params={"token": token},
	        headers={"Content-Type": "application/x-www-form-urlencoded"}
	    )
	    assert resp.ok, resp.text
	    #logout_user()        # Delete Flask-Login's session cookie
	    del blueprint.token  # Delete OAuth token from storage
	    return redirect(url_for('index'))
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
