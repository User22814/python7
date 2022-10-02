from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home_view():
    return f"<h1>Random integer = {randint(1, 1000)}</h1>"
