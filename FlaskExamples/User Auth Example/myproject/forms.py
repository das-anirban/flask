from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	username = StringField('Username', validators = [DataRequired()])
	password  = PasswordField('Password', validators = [DataRequired(), EqualTo('password_confirm', 
																				message='Passwords Donot Match')])
	password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	def check_email(self,field):
		if User.query.filter_by(email=field.data).first(): #This checks if the email is already present in database
			raise ValidationError("Email already resgitered")

	def check_username(self, field):
		if User.query.filter_by(username = field.data).first():
			raise ValidationError("Username already taken")

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password  = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField("Log in")
