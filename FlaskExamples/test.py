from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/add_two_nums',methods=['POST'])
def add_two_nums():
	# Get two nums
	dataDict = request.get_json()

	x = dataDict["num1"]
	y = dataDict["num2"]



	# Add and store

	total = x + y

	# Prepare json file for return
	response = {
	"total": total
	}

	# Return json
	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)