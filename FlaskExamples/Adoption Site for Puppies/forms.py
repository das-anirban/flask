#from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField

class AddForm(FlaskForm):

	name = StringField("Name of Puppy: ")
	submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):

	uid = IntegerField("Id number of puppy to remove: ")
	submit = SubmitField("Remove Puppy")

class AddOwner(FlaskForm):

	ownername = StringField("Enter owner name please: ")
	#puppy_id = RadioField("Please select puppy: ", choices = [('Hello','hello')])
	puppy_id = IntegerField("Enter puppy Id: ")
	submit = SubmitField("Add Owner")