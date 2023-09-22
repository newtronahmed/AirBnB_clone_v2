#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask

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
	return f"C {text}"

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
	"""display python followed by the value of the text"""
	text = text.replace("_", " ")
	return f"Python {text}"

if __name__ == "__main__":
	app.run("0.0.0.0", port=5000)