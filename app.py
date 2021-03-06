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
chains_coll = mongo.db.chains


@app.route('/')
def home():
    """
    Function for loading the home page and showing
    existing stories. Newest stories are shown first.
    """
    stories = stories_coll.find().sort('_id', -1)
    return render_template('pages/home.html',
                           stories=stories)


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Function for registering a new user.
    Also checks if username and/or password
    already exists in the database.
    Redirects to profile
    """
    # Checks if user is not already logged in
    if 'user' in session:
        flash('You are already registered!')
        return redirect(url_for('home'))
    # Checks if the passwords match
    if request.method == "POST":
        form = request.form.to_dict()
        if form['password'] == form['password1']:
            registered_user = users_coll.find_one(
                            {"username": form['username']})
    # Checks if username already exists
            if registered_user:
                flash("Username already taken")
                return redirect(url_for('register'))
    # Hashes the password and puts new user in db
            else:
                hashed_password = generate_password_hash(form['password'])
                users_coll.insert_one(
                    {
                        'username': form['username'],
                        'password': hashed_password
                    }
                )
                user_in_db = users_coll.find_one(
                        {"username": form['username']})
                if user_in_db:
                    session['user'] = user_in_db['username']
                    flash("Account successfully created")
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
    # Only visible for users who are logged in
    if 'user' in session:
        user_in_db = users_coll.find_one({"username": session['user']})
        if user_in_db:
            flash("You are logged in already!")
            return redirect(url_for('profile',
                            user=user_in_db['username']))
    else:
        return render_template('pages/authentication.html')


@app.route('/userauth', methods=["POST"])
def user_auth():
    """
    Authentication function. Makes sure the passwords
    match before a user is logged in
    """
    form = request.form.to_dict()
    user_in_db = users_coll.find_one({"username": form['username']})
    if user_in_db:
        if check_password_hash(user_in_db['password'],
                               form['password']):
            if form['password'] == form['password1']:
                session['user'] = form['username']
                flash("You were logged in")
                return redirect(url_for('profile',
                                user=user_in_db['username']))
            else:
                flash("Wrong password or username")
                return redirect(url_for('log_in'))
        else:
            flash("Passwords don't match")
            return redirect(url_for('log_in'))
    else:
        flash("You must be registered")
        return redirect(url_for('register'))


@app.route('/logout')
def log_out():
    """
    Allows the user to log out
    Takes user back to home
    """
    session.clear()
    stories = list(stories_coll.find())
    flash("You were logged out")
    return render_template("pages/home.html",
                           stories=stories)


@app.route('/profile/<user>', methods=["GET", "POST"])
def profile(user):
    """
    This function renders the profile page. This page displays the stories
    submitted by the currently logged in user and is only visible for that
    user. Newest stories are shown first.
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


@app.route('/change/password/<username>', methods=["GET", "POST"])
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
        users_coll.update({"username": username}, submit)
        flash("Your password has been updated")
        return redirect(url_for("profile",
                                user=session["user"]))
    if session:
        return render_template("pages/account.html",
                               username=username)
    return redirect(url_for("log_in"))


@app.route('/change/username/<username>', methods=["GET", "POST"])
def change_username(username):
    """
    This function renders the change username page, where a logged
    in user can change the username.
    """
    if request.method == "POST":
        registered_user = users_coll.find_one(
                            {"username": request.form['new-username']})
        if registered_user:
            flash("Username already taken")
            return redirect(url_for('change_username',
                                    username=session["user"]))
        else:
            users_coll.update_one(
                {"username": username},
                {"$set": {"username": request.form["new-username"]}},
                upsert=True)
        flash("Username updated. Please login with your new username")
        session.pop("user", None)
        return redirect(url_for("log_in"))

    return render_template("pages/account.html",
                           username=session["user"],
                           changeusername=True)


@app.route('/delete/account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    """
    This function removes a user from the "users" collection
    in the database. It removes the user from the session
    cookies and redirects to the homepage.
    A modal pops up that asks for the users password
    to have some extra security.
    """
    # Only visible for logged in user
    if 'user' not in session:
        flash('You must be logged in to delete an account!')
        return redirect(url_for("log_in"))
    user = users_coll.find_one({"_id": ObjectId(user_id)})
    # Defensive programming to assure no one else does this
    # Checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm-password-to-delete")):
        flash("Your account has been deleted.")
        session.pop("user")
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("log_in"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("profile", user=user.get("username")))


@app.route('/add/story/', methods=["GET", "POST"])
def add_story():
    """
    Allows a user to add a new story, after successful
    submit, he is redirected to the homepage.
    """
    if request.method == "POST":
        date_created = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')
        story = {
            "story_title": request.form.get("story-title"),
            "story_content": request.form.get("story-content"),
            "author": session["user"],
            "created_on": date_created,
            "story_chains": []
        }
        stories_coll.insert_one(story)
        flash("Story Successfully Added")
        return redirect(url_for("home"))

    return render_template("pages/story.html", story=True)


@app.route('/edit/story/<story_id>', methods=["GET", "POST"])
def edit_story(story_id):
    """
    Allows the user that has created the story,
    to edit the story. After doing so,
    the user is then redirected to the 'Read Story' page.
    """
    if request.method == "POST":
        created_on = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')
        submit = {
            "story_title": request.form.get("story-title"),
            "story_content": request.form.get("story-content"),
            "author": session["user"],
            "created_on": created_on,
            "edited": True
        }
        stories_coll.update({"_id": ObjectId(story_id)}, {"$set": submit})
        flash("Edit story successful")
        return redirect(url_for("read_story",
                        story_id=story_id,
                        edited=True))

    story = stories_coll.find_one({"_id": ObjectId(story_id)})
    return render_template("pages/story.html",
                           story=story)


@app.route('/delete/story/<story_id>', methods=["GET", "POST"])
def delete_story(story_id):
    """
    This functions allows for the user to delete their story.
    Because this action cannot be undone, a modal is shown
    to ask the user if he is sure.
    """
    stories_coll.remove({"_id": ObjectId(story_id)})
    flash("Your story has been removed")
    return redirect(url_for("home"))


@app.route('/chains/<story_id>', methods=["GET", "POST"])
def chains(story_id):
    if request.method == "POST":
        created_on = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')
        new_chain = {
            "chain_content": request.form.get("chain-content"),
            "author": session["user"],
            "created_on": created_on
        }
        # Inserts the new chain to the chains-collection
        insert_chain_inDB = chains_coll.insert_one(new_chain)
        # Updates the story with this chain-id
        # Pushes chain ID into the story_chains array
        stories_coll.update_one({"_id": ObjectId(story_id)},
                                {"$push": {"story_chains":
                                 insert_chain_inDB.inserted_id}})
        flash("Insert chain successful")
        return redirect(url_for("read_story",
                        story_id=story_id))

    return render_template("pages/chain.html",
                           story_id=story_id, chain=True)


@app.route('/read/story/<story_id>')
def read_story(story_id):
    """
    Displays whole story. Also gives the author of the
    story two buttons, to edit or delete the story.
    """
    # Finds the story connected to the "Read More" link
    story = stories_coll.find_one({"_id": ObjectId(story_id)})
    # Create an empty list for the chains that need to chain to the story
    chains_list = []
    # Loops over the ObjectId's in the story_chains array in the story document
    for chain in story["story_chains"]:
        temp_chain = chains_coll.find_one({"_id": ObjectId(chain)})
        # pushes those chain id's into the empty list)
        chains_list.append(temp_chain)
    return render_template("pages/readstory.html",
                           story=story,
                           chains_list=chains_list)


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/404.html", error=error), 404


@app.errorhandler(500)
def something_went_wrong(error):
    """
    Renders a custom 500 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/500.html", error=error), 500


@app.errorhandler(401)
def permission_denied(error):
    """
    Renders a custom 401 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/401.html", error=error), 401


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Renders a custom 405 error page with a button
    that takes the user back home
    """
    return render_template("/components/errors/405.html", error=error), 405


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
