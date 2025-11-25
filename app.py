from flask import Flask, render_template

app = Flask(__name__)  # initialize the class with name application.


@app.route("/")
def index():
    return render_template("index.html")
