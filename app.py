import os
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
        flash("Thank you and welcome! Let the fun begin!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/authentication.html", register=True)


@app.route('/log-in', methods=["GET", "POST"])
def log_in():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for("profile"))
            else:
                flash("Incorrect username and/or password. Please try again.")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect username and/or password. Please try again.")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """
    This function renders the profile page. This page displays the stories
    submitted by the currently logged in user and is only visible for that
    user.
    """
    #this can maybe go once new add_content function works
    #content = list(mongo.db.stories.find(add_content).sort('_id', -1))
    stories = list(mongo.db.stories.find().sort('_id', -1))
    if session:
        return render_template("pages/profile.html",
        username=session["user"],
        stories=stories)
        #add_content=add_content)

    return redirect(url_for("log_in"))


@app.route("/change/password/<username>", methods=["GET", "POST"])
def change_password(username):
    """
    This function renders the change password page which is only
    visible for the logged in user.
    """
    if request.method == "POST":
        submit = {
            "username": session["user"],
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.update({"username": username.lower()}, submit)
        flash("Your password has been updated")
        return redirect(url_for("profile", username=session["user"]))

    if session:
        return render_template("pages/change_password.html", username=username)

    return redirect(url_for("log_in"))


@app.route("/logout")
def log_out():
    """
    Allows the user to log out
    Takes user back to home
    """
    session.clear()
    stories = list(mongo.db.stories.find())
    return render_template("pages/home.html", stories=stories)


@app.route('/add_story', methods=["GET", "POST"])
def add_story():
    """
    Allows a user to add a new story
    """
    if request.method == "POST":
        story = {
            "story_title": request.form.get("story_title"),
            "story_summary": request.form.get("story_summary"),
            "story_content": request.form.get("story_content"),
            "Author": session["user"]
        }
        mongo.db.stories.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/add_story.html")


@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    """
    Allows the user that has created the story,
    to edit the story. After doing so,
    the user is then redirected to the 'Read Story' page.
    """
    if request.method == "POST":
        submit = {
            "story_title": request.form.get("story_title"),
            "story_summary": request.form.get("story_summary"),
            "story_content": request.form.get("story_content"),
            "author": session["user"]
        }
        mongo.db.stories.update({"_id": ObjectId(story_id)}, submit)
        flash("Story Successfully Updated")
        return redirect(url_for("read_story", story_id=story_id))

    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/edit_story.html", story=story)


@app.route('/read_story/<story_id>')
def read_story(story_id):
    """
    Displays whole story.
    """
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/read_story.html",
                            story=story,
                            add_content=add_content) #this can dissapear as soon as the add_content function works


@app.route('/add_content<story_id>', methods=["GET", "POST"])
def add_content(story_id):
    """
    Let's an a logged in user add content to
    an existing story.
    Redirects to profile
    """
    if request.method == "POST":
        add_content = {
            "_id": ObjectId(),
            "add_content": request.form.get("add_content"),
            "created_by": session["user"]
        }
        insert_content_intoDB = mongo.db.stories.insert_one(add_content)
        mongo.db.stories.update_one(
            {"_id": ObjectId(story_id)},
            {"$push": {"add_content": insert_content_intoDB.inserted_id}})

        flash("Content Successfully Added")
        return redirect(url_for("profile",
                        add_content=insert_content_intoDB.inserted_id,
                        username=session["user"], story_id=story_id))

    return render_template("pages/add_content.html", story_id=story_id)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
