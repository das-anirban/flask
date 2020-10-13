from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField

class AddForm(FlaskForm):

	name = StringField("Name of Puppy: ")
	submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):

	uid = IntegerField("Id number of puppy to remove: ")
	submit = SubmitField("Remove Puppy")