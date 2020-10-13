from flask import Flask,request,jsonify
from flask_restful import Api,Resource

app = Flask(__name__)

class Add(Resource):
	def post(self):
		requestDict = request.get_json()
			
		if 'x' not in requestDict or 'y' not in requestDict:
			response_code = 301

		else:
			total = requestDict['x'] + requestDict['y']
			response_code = 200

		if response_code == 301:
			response_json = {
				"Message" : "Error Occured",
				"Status" : response_code
			}
		else:
			response_json = {
				"Message" : total,
				"Status" : response_code
			}
		return jsonify(response_json)

api = Api(app)
api.add_resource(Add, '/add')

@app.route('/')
def index():
	return "<h1>Welcome</h1"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')