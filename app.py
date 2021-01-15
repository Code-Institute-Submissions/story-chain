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
    Function for loading the home page
    """
    return render_template('pages/home.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows the user to register at the website
    Checks if username already exists in Database
    Redirects user to the dashboard
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
            title = mongo.db.stories.find({"title": request.form.get("title")})
            stories = mongo.db.stories.find({"title": title})
            return redirect(url_for("profile", user_id=user_id,
                                    stories=stories))

    return render_template("pages/register.html", register=True)


@app.route('/login', methods=["GET", "POST"])
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

                profile = mongo.db.user.find_one({"user_id": user_id})

                if profile:
                    user_id = profile["_id"]
                    return redirect(url_for("profile", username=session["user"], ))
            else:
                flash("Incorrect username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            flash("Incorrect username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("pages/authenticate.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
