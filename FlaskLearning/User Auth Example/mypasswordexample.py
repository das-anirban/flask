from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

pwd = 'mycustompassword'

hashed_password = bcrypt.generate_password_hash(password = pwd)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
print(check)

check = bcrypt.check_password_hash(hashed_password, 'mycustompassword')
print(check)

from werkzeug.security import generate_password_hash, check_password_hash

hashed_pwd = generate_password_hash('mypassword')
print(hashed_pwd)

check = check_password_hash(hashed_pwd,'mypwd')
print(check)