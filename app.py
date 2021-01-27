import os
from datetime import datetime
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

        # put the new user into 'session' cookie
        if mongo.db.users.find_one({'username': username}) is not None:
            user = mongo.db.users.find_one({'username': username})
            user_id = user['_id']
            session['user_id'] = str(user_id)
            flash("Thank you and welcome! Let the fun begin!")
            return redirect(url_for("profile", user_id=user_id))

    return render_template("pages/authentication.html", register=True)


@app.route('/login', methods=["GET", "POST"])
def log_in():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                user_id = str(existing_user['_id'])
                session['user_id'] = str(user_id)

                return redirect(url_for("profile", user_id=user_id))

            else:
                flash("Incorrect username and/or password. Please try again.")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect username and/or password. Please try again.")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route("/logout")
def log_out():
    """
    Allows the user to log out
    Takes user back to home
    """
    session.clear()
    stories = list(mongo.db.stories.find())
    return render_template("pages/home.html", stories=stories)


@app.route("/profile/<user_id>", methods=["GET", "POST"])
def profile(user_id):
    """
    This function renders the profile page. This page displays the stories
    submitted by the currently logged in user and is only visible for that
    user.
    """
    stories = list(mongo.db.stories.find().sort('_id', -1))
    existing_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if existing_user is None:
        return redirect(url_for('log_in'))

    if session.get('user_id'):
        if session['user_id'] == str(existing_user["_id"]):
            return render_template("pages/profile.html", user_id=user_id,
                    stories=stories)


@app.route("/change/password/<user_id>", methods=["GET", "POST"])
def change_password(user_id):
    """
    This function renders the change password page which is only
    visible for the logged in user.
    """
    username_edit = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if request.method == "POST":
        if username_edit:
            if check_password_hash(username_edit["password"],
            request.form.get("password")):
                user_id = str(username_edit['_id'])
                session['user_id'] = str(user_id)
            mongo.db.users.update({'_id': ObjectId(user_id)},
            {"password": generate_password_hash(request.form.get("password"))})
            flash("Your password has been updated")
            return redirect(url_for("profile", user_id=user_id))

    return render_template("pages/account_settings.html", submit=True, user_id=user_id)



@app.route("/change/username/<user_id>", methods=["GET", "POST"])
def change_username(user_id):
    """
    This function renders the change username page, where a logged
    in user can change the username.
    """
    username_edit = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    if request.method == "POST":
        if username_edit:
            if check_password_hash(username_edit["password"],
            request.form.get("password")):
                user_id = str(username_edit['_id'])
                session['user_id'] = str(user_id)
            mongo.db.users.update({'_id': ObjectId(user_id)},
            {"username": request.form.get("new_username")})

        flash("Your username has been updated.")
        return redirect(url_for("log_in"))

    return render_template("pages/account_settings.html",
                            user_id=user_id)


@app.route("/delete/account/<user_id>")
def delete_account(user_id):
    """
    This function removes a user from the "users" collection
    in the database. Ti removes the user from the session
    cookies and redirects to the homepage
    """
    username_edit = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if username_edit:
        if check_password_hash(username_edit["password"], request.form.get("password")):
            user_id = str(username_edit['_id'])
            session['user_id'] = str(user_id)
        mongo.db.users.remove({'_id': ObjectId(user_id)})
        session.pop("user_id")
        flash("Your account has been removed. Sad to see you go!")
        return redirect(url_for("home"))


@app.route("/add/story/", methods=["GET", "POST"])
def add_story():
    """
    Allows a user to add a new story
    """
    if request.method == "POST":
        date_created = datetime.today().strftime('%Y-%m-%d')
        story = {
            "story_title": request.form.get("story_title"),
            "story_summary": request.form.get("story_summary"),
            "story_content": request.form.get("story_content"),
            "Author": session["user"],
            "created_on": date_created
        }
        mongo.db.stories.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("profile"))

    return render_template("pages/story.html", story=True)


@app.route("/edit/story/<story_id>", methods=["GET", "POST"])
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
            "Author": session["user"]
        }
        mongo.db.stories.update({"_id": ObjectId(story_id)}, submit).maxTimeMS(86400000)
        flash("Story Successfully Updated")
        return redirect(url_for("read_story", story_id=story_id))

    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/story.html", story=story)


# Make function for delete story, only for admin user


@app.route('/read/story/<story_id>')
def read_story(story_id):
    """
    Displays whole story.
    """
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/read_story.html",
                            story=story)


@app.route('/add/content<story_id>', methods=["GET", "POST"])
def add_content(story_id):
    """
    Let's an a logged in user add content to
    an existing story.
    Redirects to profile
    """
    # Needs to add to the story document
    if request.method == "POST":
        mongo.db.stories.update({"_id": ObjectId(story_id)},
        {"$push": {"add_content": [{"_id": ObjectId(),
        "add_content": request.form.get("add_content"),
        "created_by": session["user"]}]}})
        flash("Content Successfully Added")
        return redirect(url_for("profile",
                        add_content=add_content,
                        username=session["user"], story_id=story_id))

    return render_template("pages/content.html", story_id=story_id)


# Make function for delete content, admin only


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page with a button
    that takes the user back home
    """
    return render_template("/pages/error.html"), 404


@app.errorhandler(500)
def something_went_wrong(error):
    """
    Renders a custom 500 error page with a button
    that takes the user back home
    """
    return render_template("/pages/error.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
