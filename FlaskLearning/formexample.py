from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, 
					DateTimeField, RadioField, SelectField,
					TextField, TextAreaField)
from wtforms.validators import DataRequired #for making form elements required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

	name = StringField("What is your name?",validators = [DataRequired()])
	age = BooleanField("Are you above 18?")
	mood = RadioField("Please choose mood: ", choices = [('happy','Happy'),('sad','Sad'),('excited','Excited')])
	food = SelectField(u"Please select your food choices", choices = [('fish','Fish'),('chicken','Chicken'),
																		('veg','Vegeterian'),('mutton','Mutton')])
	feedback = TextAreaField("Enter your feedback")
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])

def index():

	form = InfoForm()

	if form.validate_on_submit():
		session['name'] = form.name.data
		session['age'] = form.age.data
		session['mood'] = form.mood.data
		session['food'] = form.food.data
		session['feedback'] = form.feedback.data
		#form.name.data = ""
		flash("Thank you for submitting")
		return redirect(url_for('thankyouform'))
		
	return render_template('home.html', form=form)

@app.route('/thankyouform')
def thankyouform():
	return render_template('thankyouform.html')

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>Page Not Found", 404

if __name__ == '__main__':
	app.run()