from myproject import db

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