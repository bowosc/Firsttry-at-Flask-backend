from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for, session
import sqlalchemy



views = Blueprint(__name__, "views")


#renders index.html
@views.route("/")
def home():
    return render_template("index.html", name="john")


#username / sign-in page



"""
assorted things to try

#query parameter (/views/profile?name=bob)
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

#json, with python dictionary thing
@views.route("/json")
def get_json():
    return jsonify({'name': 'bob', 'coolness': '10'})

#somethign about data input?
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#how to redirect page
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))
"""