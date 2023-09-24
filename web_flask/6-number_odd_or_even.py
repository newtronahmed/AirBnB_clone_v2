#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
	"""Returns string when the / route is visited"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""/hbnb: disply Hbnb"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
	"""display C followed by the value of the text"""
	text = text.replace("_", " ")
	return "C {}".format(text)

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
	"""display python followed by the value of the text"""
	text = text.replace("_", " ")
	return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
	"""display is a number only if n is an integer"""
	if type(n) == int:
		return "{} is as number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
	"""display a HTML page only if n is an integer"""
	if type(n) == int:
		return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns a template at the /number_odd_or_even/<n>
    route, display if the number is odd or even"""
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
	app.run("0.0.0.0", port=5000)
