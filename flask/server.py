
from flask import Flask, render_template, request

app = Flask(__name__)	# Start flask app

@app.route("/")	# Create route '/'
def showMain():	# Render template 'index.html' in '/'
	return render_template('index.html')

@app.route('/page1')	# Create route '/page1'
def showPage1():	# Render template 'page1.html' in '/page1'
	return render_template('page1.html')

@app.route('/signUp', methods=['POST'])
def signUp():
	name = request.form['inputName']
	email = request.form['inputEmail']
	password = request.form['inputPassword']
	print(name, email, password)
    

if __name__ == "__main__":
	app.run()

