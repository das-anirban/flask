from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('base.html')

@app.route('/<name>')
def greet(name):
	return render_template('basic.html', name=name, char=list(name)) #Like this lists, 
	#dict and others can also be sent to html. This is jinja templating

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
	first = request.args.get('firstname')
	last = request.args.get('lastname')

	return render_template('thankyou.html', first = first, last = last)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('pagenotfound.html'), 404

if __name__ == '__main__':
	app.run()