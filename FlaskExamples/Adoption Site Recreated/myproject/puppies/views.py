from flask import Blueprint, render_template, url_for, redirect, flash
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add():
	form = AddForm()

	if form.validate_on_submit():

		name = form.name.data

		new_pup = Puppy(name)
		db.session.add(new_pup)
		db.session.commit()

		flash('Puppy added successfully')
		return redirect(url_for('puppies.add'))
	return render_template('add.html', form=form)

@puppies_blueprint.route('/list')
def list():
	puppies = Puppy.query.all()
	return render_template('list.html', puppies = puppies)

@puppies_blueprint.route('/delete', methods=['GET','POST'])
def delete():
	form = DelForm()

	if form.validate_on_submit():

		uid = form.uid.data
		puppy = Puppy.query.get(uid)

		db.session.delete(puppy)
		db.session.commit()

		flash('Puppy deleted successfully')
		return redirect(url_for('puppies.delete'))
	return render_template('delete.html', form=form)