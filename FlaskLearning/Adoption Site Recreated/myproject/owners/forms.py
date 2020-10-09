from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField

class AddForm(FlaskForm):

	ownername = StringField("Enter owner name please: ")
	#puppy_id = RadioField("Please select puppy: ", choices = [('Hello','hello')])
	puppy_id = IntegerField("Enter puppy Id: ")
	submit = SubmitField("Add Owner")