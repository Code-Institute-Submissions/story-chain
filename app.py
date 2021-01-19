import os
import pymongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def home():
    """
    Function for loading the home page and showing
    existing stories.
    """
    stories = list(mongo.db.stories.find())
    return render_template('pages/home.html', stories=stories)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function for registering a new user.
    Also checks if username and/or password
    already exists in the database.
    Redirects to profile
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/authentication.html", register=True)


@app.route('/log-in', methods=["GET", "POST"])
def log_in():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route('/profile', methods=["GET", "POST"])
def profile():
    """
    This function renders the profile page. This page displays the images
    uploaded by the currently logged in user and is only visible for him.
    """
    stories = list(mongo.db.stories.find().sort('_id', -1))
    if session:
        return render_template('pages/profile.html',
        username=session["user"], stories=stories)

    return redirect(url_for("log_in"))


@app.route('/logout')
def log_out():
    """
    Allows the user to log out
    Takes user back to home
    """
    session.clear()
    return render_template("pages/home.html")


@app.route('/add_story', methods=["GET", "POST"])
def add_story():
    """
    Allows a user to add a new story
    """
    if request.method == "POST":
        story = {
            "story_title": request.form.get("story_title"),
            "story_content": request.form.get("story_content"),
            "created_by": session["user"]
        }
        mongo.db.stories.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/add_story.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
