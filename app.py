from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

#from views import views

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
#bonus line of code, not sure if neccessary
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=2)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


#app.register_blueprint(views, url_prefix="/views")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Your email has been saved.")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    
    else:
        flash("You aren't logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out.", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))
 


if __name__ == '__main__':
    #make database if none exists
    with app.app_context():
        db.create_all()
    #idk what this is, this has been here since day 1
    app.run(debug=True, port=8000)