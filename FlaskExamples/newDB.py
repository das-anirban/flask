from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db) # Adds this app i.e. newDB.py to the database for migration capabilities. Migration like adding new columns and other updates

# Then in the command line terminal enter the following command
# FLASK_APP = newDB.py - sets up the environment variable
# flask db init -  sets up the migration directory
# flask db migrate -m "created UsersTable"
# flask db upgrade - upgrades and performs the migration

# These above lines create a database for our application and data.sqlite is the actual database file
##############################################################################################

class UserInfo(db.Model):

	# Manually setting the table name
	__tablename__ = 'UsersTable'

	uid = db.Column(db.Integer, primary_key=True) # Creates a column named id and sets it as Primary Key
	name = db.Column(db.Text)
	age = db.Column(db.Integer)

	#adding this column after adding flask_migrate
	gender = db.Column(db.Text)

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __repr__(self): # repr means representation - means what happens when user prints the object
		return "{} is {} years old and is {}".format(self.name, self.age, self.gender)

#if __name__ == '__main__':
#	app.run()