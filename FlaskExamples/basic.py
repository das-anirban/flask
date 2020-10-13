from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello There</h1>"

@app.route('/author')
def author():
	return "<h1>Anirban Das</h1"

#Dynamic Route	
@app.route('/puppy/<name>')
def puppyname(name):
	return "<h1>This is a page for {}</h1>".format(name)

#Example of debugging
@app.route('/charatindex/<string>/<index>')
def getcharacter(string, index):
	index = int(index)
	return "<p>The character at index {} for string {} is {}".format(index, string, string[index])

#PuppyLatin Code Exercise
@app.route('/puppylatin/<puppyname>')
def puppylatinmaker(puppyname):

	if puppyname[len(puppyname)-1].lower() == 'y':
		latinname = puppyname[:len(puppyname)-1] + 'iful'

	else:
		latinname = puppyname + 'y'

	return "<h1>Latin name for the puppy {} is {}</h1>".format(puppyname, latinname)


if __name__ == '__main__':
	app.run()