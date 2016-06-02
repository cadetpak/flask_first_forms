from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template("index.html")

#this route will handle form submission
@app.route('/create', methods=['POST'])
def create_user(): 
	# name = request.form['name']
	# location = request.form['location']
	# language = request.form['language']
	# comment = request.form['comment']

	return render_template("create.html", name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

app.run(debug=True)