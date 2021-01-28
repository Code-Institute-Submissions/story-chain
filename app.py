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
    # checks if user is not already logged in
    if 'user' in session:
        flash('You are already registered!')
        return redirect(url_for('home'))

    if request.method == "POST":
        form = request.form.to_dict()
        if form['password'] == form['password1']:
            registered_user = users_coll.find_one({"username": form['username']})

            if registered_user:
                flash("Username already taken")
                return redirect(url_for('register'))

            else:
                hashed_password = generate_password_hash(form['password'])
                
                users_coll.insert_one(
                    {
                        'username': form['username'],
                        'password': hashed_password
                    }
                )
                user_in_db = users_coll.find_one({"username": form['username']})
                if user_in_db:
                    session['user'] = user_in_db['username']
                    return redirect(url_for('profile', user=user_in_db['username']))

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
            # If so redirect user to his profile
            flash("You are logged in already!")
            return redirect(url_for('profile', user=user_in_db['username']))

    else:
            # Render the page for user to be able to log in
        return render_template('pages/authentication.html')


@app.route('/user_auth', methods=['POST'])
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
            return redirect(url_for('login'))

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
    stories = list(mongo.db.stories.find())
    return render_template("pages/home.html", stories=stories)


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    """
    This function renders the profile page. This page displays the stories
    submitted by the currently logged in user and is only visible for that
    user.
    """
    if 'user' in session:
        user_in_db = users_coll.find_one({"username": user})
        return render_template('pages/profile.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('home'))


@app.route("/change/username/<user>", methods=["GET", "POST"])
def change_username(user):
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


@app.route("/delete/account/<user>")
def delete_account(user):
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


@app.route('/add/content<story_id>, <user>', methods=["GET", "POST"])
def add_content(story_id, user):
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
                        user=user, story_id=story_id))

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
