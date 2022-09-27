from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def hello_world():
    lists = ""
    for i in range(666):
        lists += f"<li><strong>{randint(1, 666)}</li>"

    return f"<ul>{lists}</ul>"
