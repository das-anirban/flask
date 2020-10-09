# Using this for model.py
# Create entries for tables in model.py

from model import db, Puppy, Toy, Owner

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())

print(rufus.report_toys())

rufus = Puppy.query.filter_by(name='Rufus').first() #Gives the first puppy with name puppy

anirban = Owner('Anirban',rufus.uid)

toy1 = Toy('Chew Toy', rufus.uid)
toy2 = Toy('Ball', rufus.uid)
toy3 = Toy('Soft Toy', rufus.uid)

db.session.add_all([anirban,toy1,toy2,toy3])
db.session.commit()

#Grab Rufus again

rufus = Puppy.query.filter_by(name='Rufus').all()[0]
print(rufus)

rufus.report_toys()