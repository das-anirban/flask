from user import User

users = [User(1,'Anirban','admin'), User(2,'Nupur','admin')]

username_table = {u.username: u for u in users}
userid_table = {u.id:u for u in users}

def authenticate(username,password):
	user = username_table.get(username, None)
	if user and password == user.password:
		return user

def identity(payload):
	user_id = payload['identity']
	return userid.table.get(user_id, None)

