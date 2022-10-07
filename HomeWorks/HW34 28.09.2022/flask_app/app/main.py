from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates')


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/todo_create/")
def todo_create():
    return render_template('todo_create.html')

