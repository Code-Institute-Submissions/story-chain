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

        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one({
            'username': username,
            'password': password})

        if mongo.db.users.find_one({'username': username}) is not None:
            user = mongo.db.users.find_one({'username': username})
            user_id = user['_id']
            session['user_id'] = str(user_id)
            stories = mongo.db.stories.find({"user_id": user_id})
            story_count = stories.count()
            return redirect(url_for("empty_profile",
                                    user_id=user_id,
                                    story_count=story_count))

    return render_template("pages/authentication.html", register=True)


@app.route("/log-in", methods=["GET", "POST"])
def log_in():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            if check_password_hash(user["password"],
                request.form.get("password")):
                user_id = str(user['_id'])
                session['user_id'] = str(user_id)

                story = mongo.db.stories.find_one({"user_id": user_id})

                if story:
                    story_id = story["_id"]
                    stories = mongo.db.stories.find({"user_id": user_id})
                    story_count = stories.count()
                    return redirect(url_for("filled_profile",
                                            user_id=user_id,
                                            story_id=story_id,
                                            story_count=story_count))

                else:
                    stories = mongo.db.stories.find({"user_id": user_id})
                    story_count = stories.count()
                    return redirect(url_for("empty_profile",
                                            user_id=user_id,
                                            story_count=story_count))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route("/profile/<user_id>")
def empty_profile(user_id):
    """
    When a user hasn't written any stories yes,
    this function renders an empty profile page.
    """
    stories = mongo.db.stories.find({"user_id": user_id})
    story_count = stories.count()
    return render_template('pages/profile.html',
                            user_id=user_id,
                            story_count=story_count)


@app.route("/profile/<user_id>/<story_id>", methods=["GET", "POST"])
def filled_profile(user_id, story_id):
    """
    When a user has written at least one story,
    this will be displayed on the profile.
    """
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    stories = mongo.db.stories.find({"user_id": user_id})
    story_count = stories.count()

    if user is None:
        return redirect(url_for("sign_in"))

    if session.get('user_id'):
        if session['user_id'] == str(user["_id"]):
            stories = list(mongo.db.stories.find().sort('_id', -1))
            return render_template('pages/profile.html',
                            user_id=user_id,
                            story_count=story_count,
                            story_id=story_id)



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
            "created_by": session["user"]
        }
        mongo.db.stories.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/add_story.html")


@app.route('/read_story/<story_id>')
def read_story(story_id):
    """
    Displays whole story.
    """
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/read_story.html", story=story)


@app.route('/add_content', methods=["GET", "POST"])
def add_content():
    """
    Let's an a logged in user add content to
    an existing story.
    """
    if request.method == "POST":
        story = {
            "story_content": request.form.get("story_content"),
            "created_by": session["user"]
        }
        mongo.db.stories.insert_one(story)
        flash("Content Successfully Added")
        return redirect(url_for("read_story"))

    return render_template("pages/add_content.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
