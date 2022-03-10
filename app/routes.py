from flask import render_template, redirect, request, url_for, session

from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("home.html")
