import os
from forms import AddForm, DelForm, AddOwner
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


############################################
####### SQL Database #######################
############################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'puppy_data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###############################################
#################### MODELS ###################
###############################################

class Puppy(db.Model):

	__tablename__ = 'puppies'

	uid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	owner = db.relationship('Owner',backref='puppy',uselist=False)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		if self.owner:
			return "ID - {}. Puppy {} has owner named {}".format(self.uid, self.name, self.owner.ownername)
		else:
			return "ID - {}. Puppy {} has no owner".format(self.uid,self.name)

class Owner(db.Model):

	__tablename__ = 'owners'
	uid = db.Column(db.Integer, primary_key=True)
	ownername = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.uid'))

	def __init__(self,ownername,puppy_id):
		self.ownername = ownername
		self.puppy_id = puppy_id

	def __repr__(self):
		return "Owner name is {} with puppy_id {}".format(self.ownername, self.puppy_id)

################### View Functions #######################

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add_pup():
	form = AddForm()

	if form.validate_on_submit():

		name = form.name.data

		new_pup = Puppy(name)
		db.session.add(new_pup)
		db.session.commit()

		flash('Puppy added successfully')
		return redirect(url_for('add_pup'))
	return render_template('add.html', form=form)

@app.route('/list')
def list_pup():

	puppies = Puppy.query.all()
	return render_template('list.html', puppies = puppies)

@app.route('/delete', methods=['GET','POST'])
def del_pup():
	form = DelForm()

	if form.validate_on_submit():

		uid = form.uid.data
		puppy = Puppy.query.get(uid)

		db.session.delete(puppy)
		db.session.commit()

		flash('Puppy deleted successfully')
		return redirect(url_for('del_pup'))
	return render_template('delete.html', form=form)

@app.route('/add-owner', methods=['GET','POST'])
def add_owner():

	form = AddOwner()

	if form.validate_on_submit():
		ownername = form.ownername.data
		puppy_id = form.puppy_id.data

		newowner = Owner(ownername,puppy_id)

		db.session.add(newowner)
		db.session.commit()

		flash('Owner added successfully')
		return redirect(url_for('add_owner'))
	return render_template('add_owner.html', form = form)

if __name__ == '__main__':
	app.run(debug=True)
