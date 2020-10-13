import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'model.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Puppy(db.Model):

	__tablename__ = 'puppies'

	uid = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	# One to many relation
	# One puppy to many toys
	toys = db.relationship('Toy',backref='puppy',lazy='dynamic')

	#One to one relation
	#One puppy to one owner

	owner = db.relationship('Owner', backref='puppy',uselist=False)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		if self.owner:
			return "Puppy name is {} and owner is {}".format(self.name, self.owner.owner_name)
		else:
			return "Puppy {} has no owner yet!".format(self.name)

	def report_toys(self):
		print("Here are the toys:")
		for toy in self.toys:
			print(toy.item_name)

class Toy(db.Model):

	__tablename__ = 'toys'

	uid = db.Column(db.Integer, primary_key = True)
	item_name = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.uid')) #here puppies is the tablename and uid is the prim key

	def __init__(self,item_name, puppy_id):
		self.item_name = item_name
		self.puppy_id = puppy_id


class Owner(db.Model):
	
	__tablename__ = 'owners'

	uid = db.Column(db.Integer, primary_key=True)
	owner_name = db.Column(db.Text)

	puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.uid'))

	def __init__(self, owner_name, puppy_id):
		self.owner_name = owner_name
		self.puppy_id = puppy_id

