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


# MongoDb collection variables
users_coll = mongo.db.users
stories_coll = mongo.db.stories


@app.route('/')
def home():
    """
    Function for loading the home page and showing
    existing stories.
    """
    stories = stories_coll.find().sort('_id', -1)
    date_created = "date created (newest to oldest)"
    return render_template('pages/home.html',
                            stories=stories,
                            date_created=date_created)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function for registering a new user.
    Also checks if username and/or password
    already exists in the database.
    Redirects to profile
    """
    # checks if user is not already logged in
    if 'user' in session:
        flash('You are already registered!')
        return redirect(url_for('home'))

    if request.method == "POST":
        form = request.form.to_dict()
        if form['password'] == form['password1']:
            registered_user = users_coll.find_one(
                            {"username": form['username']})

            if registered_user:
                flash("Username already taken")
                return redirect(url_for('register'))

            else:
                hashed_password = generate_password_hash(form['password'])
                users_coll.insert_one(
                    {
                        'username': form['username'],
                        'password': hashed_password
                        # user_stories[]?
                    }
                )
                user_in_db = users_coll.find_one(
                        {"username": form['username']})
                if user_in_db:
                    session['user'] = user_in_db['username']
                    return redirect(url_for('profile',
                                    user=user_in_db['username']))
                else:
                    flash("There was a problem saving your profile")
                    return redirect(url_for('register'))
        else:
            flash("Passwords don't match")
            return redirect(url_for('register'))

    return render_template('pages/authentication.html', register=True)


@app.route('/login', methods=["GET"])
def log_in():
    """
    Allows user to sign in with username and password
    Redirects user to profile
    """
    if 'user' in session:
        user_in_db = users_coll.find_one({"username": session['user']})
        if user_in_db:
            flash("You are logged in already!")
            return redirect(url_for('profile', user=user_in_db['username']))

    else:
        return render_template('pages/authentication.html')


@app.route('/userauth', methods=["POST"])
def user_auth():
    form = request.form.to_dict()
    user_in_db = users_coll.find_one({"username": form['username']})

    if user_in_db:
        if check_password_hash(user_in_db['password'], form['password']):
            session['user'] = form['username']
            flash("You were logged in")
            return redirect(url_for('profile', user=user_in_db['username']))

        else:
            flash("Wrong password or username")
            return redirect(url_for('log_in'))

    else:
        flash("You must be registered")
        return redirect(url_for('register'))


@app.route("/logout")
def log_out():
    """
    Allows the user to log out
    Takes user back to home
    """
    session.clear()
    stories = list(stories_coll.find())
    return render_template("pages/home.html",
                            stories=stories)


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    """
    This function renders the profile page. This page displays the stories
    submitted by the currently logged in user and is only visible for that
    user.
    """
    stories = stories_coll.find().sort('_id', -1)
    story = list(stories_coll.find().sort('_id', 1))
    if 'user' in session:
        user_in_db = users_coll.find_one({"username": user})
        return render_template('pages/profile.html',
                                user=user_in_db,
                                story=story,
                                stories=stories)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


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
        users_coll.update({"username": username.lower()}, submit)
        flash("Your password has been updated")
        return redirect(url_for("profile",
                                user=session["user"]))

    if session:
        return render_template("pages/changepassword.html",
                                username=username)

    return redirect(url_for("log_in"))


@app.route("/change/username/<username>", methods=["GET", "POST"])
def change_username(username):
    """
    This function renders the change username page, where a logged
    in user can change the username.
    """
    if request.method == "POST":
        registered_user = users_coll.find_one(
                            {"username": request.form['new_username']})
        if registered_user:
            flash("Username already taken")
            return redirect(url_for('change_username',
                                    username=session["user"]))
        else:
            users_coll.update_one(
                {"username": username},
                {"$set": {"username": request.form["new_username"]}},
                            upsert=True)
        flash("Your username has been updated. Please login with your new username")
        session.pop("user", None)
        return redirect(url_for("log_in"))

    return render_template("pages/changeusername.html",
                            username=session["user"])


@app.route("/delete/account/<user_id>", methods=["GET", "POST"])
def delete_account(user_id):
    """
    This function removes a user from the "users" collection
    in the database. Ti removes the user from the session
    cookies and redirects to the homepage
    """
    if 'user' not in session:
        flash('You must be logged in to delete an account!')
        return redirect(url_for("log_in"))
    user = users_coll.find_one({"_id": ObjectId(user_id)})
    # checks if password matches existing password in database
    if check_password_hash(user["password"],
    request.form.get("confirm_password_to_delete")):
        flash("Your account has been deleted.")
        session.pop("user")
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("log_in"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("profile", user=user.get("username")))


@app.route("/add/story/", methods=["GET", "POST"])
def add_story():
    """
    Allows a user to add a new story
    """
    if request.method == "POST":
        date_created = datetime.today().strftime('%m/%d/%Y')
        story = {
            "story_title": request.form.get("story_title"),
            "story_content": request.form.get("story_content"),
            "Author": session["user"],
            "created_on": date_created
        }
        stories_coll.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("home"))

    return render_template("pages/story.html", story=True)


@app.route("/edit/story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    """
    Allows the user that has created the story,
    to edit the story. After doing so,
    the user is then redirected to the 'Read Story' page.
    """

    if request.method == "POST":
        created_on = datetime.today().strftime('%m/%d/%Y')
        submit = {
            "story_title": request.form.get("story_title"),
            "story_content": request.form.get("story_content"),
            "Author": session["user"],
            "created_on": created_on
        }
        stories_coll.update({"_id": ObjectId(story_id)}, submit)
        flash("Edit story succesfull")
        return redirect(url_for("read_story",
                                story_id=story_id))

    story = stories_coll.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/story.html", 
                            story=story)


@app.route("/delete/story/<story_id>", methods=["GET", "POST"])
def delete_story(story_id):
    """
    This functions allows for the user to delete their story.
    Because this obstructs the flow of the story, a warning
    is shown
    """
    stories_coll.remove({"_id": ObjectId(story_id)})
    flash("Your story has been removed")
    return redirect(url_for("home"))


@app.route('/read/story/<story_id>')
def read_story(story_id):
    """
    Displays whole story.
    """
    story = stories_coll.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/readstory.html",
                            story=story)


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/404.html"), 404


@app.errorhandler(500)
def something_went_wrong(error):
    """
    Renders a custom 500 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/500.html"), 500


@app.errorhandler(401)
def permission_denied(error):
    """
    Renders a custom 401 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/401.html"), 401


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Renders a custom 405 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/405.html"), 405


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
