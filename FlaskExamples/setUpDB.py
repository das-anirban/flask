from newDB import db, UserInfo

db.create_all() # Transforms all the model tables to database tables. Usually this is done via command line tools and not an extra py file

# CREATE
anir = UserInfo('Anirban', 27)
nup = UserInfo('Nupur', 27)
anirup = UserInfo('Anirup', 54)

print(anir.uid) #Both these should return None because it hasn't been added to the database yet
print(nup.uid)

db.session.add_all([anir, nup]) #Multiple objects at a time
db.session.add(anirup) # Single object at a time

db.session.commit()

print(f"Anirban\'s Id is {anir.uid} and Nupur\'s Id is {nup.uid}") #Now it is added to the database
print(anir) #Example what the __repr__ actually is used for

# READ
all_users = UserInfo.query.all() #List of all user objects from the table

# Select by ID

first_user = UserInfo.query.get(1) # Targets the primary key
print(first_user.uid)

# Filter with other columns rather than primary key

some_user = UserInfo.query.filter_by(name='Anirban')
print(some_user.all()) # This will print Anirban is 27 years old

# UPDATE
first_user = UserInfo.query.get(1)
first_user.age = 30
db.session.add(first_user)
db.session.commit()


# DELETE

third_user = UserInfo.query.get(4)
db.session.delete(third_user)
db.session.commit()


#Print all users
all_users = UserInfo.query.all()
print(all_users)