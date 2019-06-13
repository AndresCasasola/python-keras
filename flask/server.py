
from flask import Flask, render_template, request
from flask import redirect, url_for

app = Flask(__name__)	# Start flask app

@app.route("/")	# Create route '/'
def showMain():	# Render template 'index.html' in '/'
	return render_template('index.html', value = 'OutputName')

@app.route("/<value>")	# Create route '/<value>'
def showMainValue(value):	# Render template 'index.html' with value=value
	return render_template('index.html', value = value)

@app.route('/page1')	# Create route '/page1'
def showPage1():	# Render template 'page1.html' in '/page1'
	return render_template('page1.html')

@app.route('/signUp', methods=['POST'])
def signUp():
	print("Sign up function")
	#name = request.form['inputName']
	#email = request.form['inputEmail']
	#password = request.form['inputPassword']
	#print(name, email, password)
	
	data = request.form
	print(data)
	response = 'Received!'
	return response

@app.route('/output', methods=['GET'])
def output():
	print("Output function")
	user = 'Andres'
	response = redirect(url_for('showMainValue', value = user))
	#response = render_template('index.html', value = user)
	return response


if __name__ == "__main__":
	app.run(host='localhost', port='5000', debug=False)

