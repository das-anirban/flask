from flask import Blueprint, render_template, url_for, redirect, flash
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')


@owners_blueprint.route('/add', methods=['GET','POST'])
def add():

	form = AddForm()

	if form.validate_on_submit():
		ownername = form.ownername.data
		puppy_id = form.puppy_id.data

		newowner = Owner(ownername,puppy_id)

		db.session.add(newowner)
		db.session.commit()

		flash('Owner added successfully')
		return redirect(url_for('owners.add'))
	return render_template('add_owner.html', form = form)