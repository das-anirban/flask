from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


api = Api(app)

jwt = JWT(app,authenticate,identity)

class HelloWorld(Resource):

	def get(self):
		return {'hello':"Hello World"}

api.add_resource(HelloWorld,'/')

puppies = []

class PuppyNames(Resource):

	def get(self, name):
		for pup in puppies:
			if pup['name'] == name:
				return pup

		return {'name': None},404

	@jwt_required
	def post(self, name):
		pup = {'name':name}

		puppies.append(pup)

		return pup

	@jwt_required
	def delete(self, name):
		for index,pup in enumerate(puppies):
			if pup['name'] == name:
				deleted_pup = puppies.pop(index)
				return {'note':'delete success'}
		return {'name': None}

class AllNames(Resource):

	def get(self):
		return {'puppies':puppies}

api.add_resource(PuppyNames, '/puppy/<String:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
	app.run(debug=True)