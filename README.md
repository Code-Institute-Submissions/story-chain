# Story Chain #
*So you think you can write?*

![Header Image](/static/images/hero-header.jpg)

## Project goals ##
Writing stories can be a lot of fun. But what if you could write stories with complete strangers? In this app you can start a new story or add to an existing story. This way, you'll never know what is going to happen, making writing both more challenging and fun!

## UX ##
### User Goals ###
* The website has to work well on all kind of devices like mobile phones, tables and desktops 
* The login procedure should be clear and feedback should be given when appropriate
* The registration process should be clear, easy to do and feedback should be given when appropriate
* The website has to be easy to use and easy to update information 
* Visually appealing website 

### Scope ###

An easy to navigate and responsive website that is fun to use and allows users to perform CRUD operations. Users can sign up and, once logged in, share their stories. These users manage their own stories, meaning they can edit and delete them when they want.
Also, they can update their password and username and even delete their account.

### Structure of the website: ###

<strong>View for a guest user:</strong>

A user that is not logged in and/or registered, will see a list of all stories on the homepage. There is also a call to action button 'Join Us!' urging them to register. They also have a navigation menu, only containing 'Home', 'Register' and 'Log In'. All other functionality is restricted to a logged in user.
They are able to click the 'Read More' button when the click a card where the title of the story is, which will lead them to the 'Read Story' page. Here they are also prompted to register/login to benefit from the full functionality of the site.

<strong>View for logged in user:</strong>

A logged in user will benefit from the full functionality of the site. The navigation will contain: 'Home', 'Profile (with their username for ease)', 'Add' and 'Logout'.
This user can then add a new story by clicking the 'Add' button in the navigation or on their profile. 
The added functionality for this user is the ability to add a story, edit that story and even delete is. This functionality is restricted for only to the user that is logged in and is also the creator of that story.
In the profile there are also functions for changing once username, password and even delete their account.
All this added functionality is also available to the site owner via an "admin" account.



### User Stories ###
* As a user, I would like to be able to register for the website so I can have my personal environment. 
* As a user, I want to login after I created an account and see my previous inserted information. 
* As a user, I would like to have a personal environment (profile page) where I can see everything I have posted. 
* As a user, I want to be able to add a new story.
* As a user, I want to be able to add content to an existing story. 
* As a user, I want to be able to edit the new story or the content I have added to an existing story.
* As a user, I want the website to be easy to use. 
* As a user, I want the process to add / edit / delete info to be easy. 
* As a user, I want to be able to logout of my profile.
* As a user, I want to be able to change my username and password.
* As a user, I want to be able to delete my account.

### Site owner goals ###
* To have an appealing website that writes use to write stories. 
* To have a great functionality so the user feels like this website enables them to practice writing or just enjoy reading what other user have wrote.
* To make the website more personal, by having everything the user has written, be on display on their profile page.

## User Requirements and Expectations
### Requirements ###
* Easy to navigate by using the few buttons 
* Appealing profile page with a functional overview 
* Easy way to add a a new story
* Easy way to add onto an existing story 
* Ability to edit and delete any entries

### Expectations ###
* When you have multiple stories, it should be easy to decern them and edit or delete them when necessary
* To have a profile page where all the necessary information is visible 
* It should be easy to add a new story or add onto an existing story

## Design Choices ##
I have based the designs for this website on the image used for the hero header. I wanted to create an atmosphere of warmth and welcome any user to join the fun.

### Colors ###
I have used [Coolors](https://coolors.co/) for creating a color scheme.

![Color scheme](/wireframes/colorscheme.png)

* #F8F8FF: This is a more off white color, to keep the more darker toned colors together and create a more warming atmosphere. This will be the background color.
* #000000: This will be the main font color. 
* #BC5609: This will be the color of the lines and borders.
* 5F2121: This will be the font color for the logo and the titles on the homepage.

I have used a contrast checker in order to make sure that the contrast is sufficient. This way my content will be easily readable.
### Fonts ###
The fonts I’ll be using are:

[Indie Flower:](https://fonts.google.com/specimen/Indie+Flower?query=Indie) For the logo, header and titles

[Raleway:](https://fonts.google.com/specimen/Raleway?query=raleway) For the content

Fonts are from [Google Fonts.](https://fonts.google.com/)

### Icons ###
Icons used are from [Font Awesome.](https://fontawesome.com/) The are used in moderation and match the colors and overall feel of the design.

### Structure ###
For the structure I have used [Bulma.](https://bulma.io/) I wanted to challenge myself to not use Bootstrap (as I have done in former projects) or Materialize, but found it important (and fun!) to use something completely different. 

## Wireframes, Flowcharts and Data Models ##

### Wireframes ###

For wireframing I have used [Pencil.](https://pencil.evolus.vn/)

View my wireframes [here](https://github.com/byIlsa/story-chain/blob/master/wireframes/wireframes.pdf).

### Flowcharts ###
I have decided to make a flowchart for the sign-in / register process to completely understand each step of the process.

You can view this below:

![Flowchart](/wireframes/flowchart.jpg)

### Data Models ###
I also created a conceptual data model to get a feel for the needed entities, relationships and attributes, which have also helped me form the user stories.

![Conceptual Data Model](/assets/wireframes/conceptualdatamodel.jpg)

#### Database Structure ####
For this project I have used [MongoDB](https://www.mongodb.com/cloud/atlas).It contains two collection, 'users' and stories'. When a user signs up, his username and hashed password are added to the users collection.
When a logged in user adds a story to the website, his username is added as a value for the key 'Author' in the stories collection.

## Features ##

### Features that are implemented ###
* Registration functionality 
* Sign-In and Out functionality 
* Add a new story
* Add to an existing story (not implemented yet, see below)
    * CRUD Functions: 
        * Create: possibility to create a new story
        * Read: home page with stories in progress that non-members can also read, as well as a profile page where members can see what the have added.
        * Update: possibility to edit the content that a member has added and change username and/or password.
        * Delete: possibility to delete content that a member has added and delete account.

### Features to be implemented ###
* Add to an existing story
    * For this project I had the idea that a logged in user should also be able to add content to an existing story, creating the 'chain'. But due to personal circumstances and that I just wasn't able to figure this one out, I had to move it to the 'left to implement' section.
    This is not for lack of trying. I have tried different ways to implement this, using the aggregating pipeline that mongo has to offer, but I sadly never was able to make it work. I do still feel strongly for this functionality and will surely try this again at a later stage, when my knowledge has grown further.
* Have a 'forget password' functionality
    * The user now has the ability to change their email. But I would really like to have a 'forgot your password' function so a user can reset it.
* Add a search functionality
    * To allow a search functionality I am thinking about having people include 'tag' words so other users could search by matching those keywords.
* A way to add the username 'guest' to stories from people who have deleted their account without them deleting their stories. The way it is right now, a new user is technically able to register that username again and own those stories.


## Technologies used ##

### Languages ###
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JS](https://nl.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### Libraries and Frameworks ###
* [Font Awesome](https://fontawesome.com/)
* [Bulma](https://bulma.io/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)

### Tools ###
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Pencil](https://pencil.evolus.vn/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Heroku](https://www.heroku.com/)
* [Github](https://github.com/)
* [Chromium](https://www.chromium.org/Home)


## Testing ##

### Testing user stories:

***Registration***

**User story: As a user, I would like to be able to register for the website so I can have my personal environment**

* A red call to action button in the hero image with the text "Join Us!" is presented. There is also a ‘register’ link in the navigation bar at the top.
When users want to register, they only have to provide a username and password. 
After registering, they will be redirected to their profile page. There they see an section with an 'add' button at the top of the screen as well as a ‘account options’ section for editing the username and/or password and deleting their account.
On this page all their submitted content is also displayed. At all stages where a user input is given, flash messages direct the user if an action was indeed successful.

* All is working as intended.

***Sign In***

**User story: As a user, I want to login after I created an account and see my previous inserted information.**

* A user can log in by clicking the 'Log In' button in the navigation. He is then directed to a login form, that prompts for the username and password. After the login is successful, the user is redirected to their profile, where an appropriate flash message is given. On the profile, when applicable, any content that is submitted by the user, is presented. Also the ability to change their username, password and delete account is given.


***Profile Page***

**User story: As a user, I would like to have a personal environment (profile page) where I can see everything I have posted.**

* After a user has had a successful login or registration, he is redirected to his personal profile page. Here he can see any previous submitted content and have full account control by having the ability to change a username, change a password and delete his account. Also a section for 'add' as story is given.


***Add new story***

**User story: As a user, I want to be able to add content to a existing story.**

* Not yet implemented, still working on this user story.

**User story: As a user, I want to be able to edit/delete content of an existing story.** 

* Not yet implemented, still working on this user story.

**User story: As a user, I want to be able to add a new story.**

* After an user is logged in, a 'Add' button appears in the navigation, as well as in their profile. This will prompt a form for them to fill. After a successful submit action, the story will be displayed on both the home page as well as their profile page. Before hitting submit, the user also has an option to cancel the action by clicking the 'cancel' button. Appropriate feedback is given by flash messages after clicking the 'submit' button.  

***Edit an existing story***

**User story: As a user, I want to be able to edit the new story.** 

* A user that is the writer of an story (and/or content) will have buttons presented under that content that allows them to edit it. This is only visible if the logged in user also matches the user that has submitted the content.
A form is given to be filled and after a successful submission, the user is redirected to the home page and presented with an appropriate flash message. There is also a button that let's the user cancel it's action and return to the home page if he should so desire.


***Delete story***

**User story: As a user, I want to be able to delete the stories I have started.**
* After clicking the 'Read More' button in a story from the home page and if the current user is also the author of the story, a 'edit' and a 'delete' button will appear. After the user clicks the 'delete' button, it will prompt a modal, warning the user that deleting the content seriously affects the flow of the story. A user can then either click a 'cancel' button which will close the modal or click 'delete' once more. This will then delete the story form the database, homepage and the profile. An appropriate flash message will be given.


***Creating, editing and deleting content to an existing story***

**User story: As a user, I want to be able to add content to a existing story.**

* Not yet implemented, still working on this user story.

**User story: As a user, I want to be able to edit/delete content of an existing story.** 

* Not yet implemented, still working on this user story.


***Account options***

**User story: As a user, I want to be able to change my username and password.**

* After a user has had an successful login, he is directed to his profile page. There they see three buttons 'Change username', 'Change password' and 'delete account'. The 'change username' button opens a small form that asks the user to enter a new username. This username is then checked against existing usernames in the database and gives appropriate feedback.

* After a user has had an successful login, he is directed to his profile page. There he can click the 'Change password' button. He is then led to a small form, asking for a new password. That password is then hashed and stored in the database.

**User story: As a user, I want to be able to delete my account.**

* After a user has had an successful login, he is directed to his profile page. There he can click the 'Delete account' button. A modal pops up, asking the user he is sure about deleting their account. After clicking "I'm sure", their account is deleted from the database. 

***Log out***

**User story: As a user, I want to be able to log out of my profile.**

* Once a user is logged in, in the navigation, a button appears that has the text 'Log Out' on it. Once clicked, the user is logged out and returned to the homepage. An appropriate flash message will be displayed.

## Manual testing ##

# Home
* On the homepage, all stories are displayed in cards. They are collapsible, only showing the title and the date they where posted. When clicking on the title, a 'teaser' appears. In the navigation the 'Home', 'Register' and 'Log In' buttons are visible to users without an account. More options will become available as soon as a user has registered or logged in.

# Register
* Before signing up, users see the options Home, Register and Log In in the navigation bar.
* In the Register form: provide username of less than 2 characters. The form tells a user that the username doesn't meet the criteria (validation message). A help message has been displayed beneath the form field stating: "Only letters (either case) and numbers. No special characters"
* Provide a password of less than 5 characters. The form tells a user that the password doesn't meet the criteria (validation message). A help message has been displayed beneath the form field stating: "Only letters (either case) and numbers, 6 or more characters".
* Leave one or more fields empty. The form tells a user that the empty field needs to be filled in (validation message).
* Provide username or password containing forbidden characters. Only a-z, A-Z, and 0-9 are allowed. The form tells a user that the username or password don't meet the criteria (validation message).
* Provide a username that already exists and submit the form. The user is redirected back to the sign up page. A flash message is visible: 'Username already taken.'
* Provide a username and password that meet the criteria, the user is added to the 'users' collection in the database and redirected to their profile page.  On the website, the user sees the options Home, Profile, Add and Log Out in the navigation bar.

# Log In



## Bugs

### In development:

**Name:** Navbar collapse not working.

* Bug description:
After finishing the basic and extended navbar, I quickly noticed that the hamburger menu wasn't behaving as expected.

* Fix:
 I looked on the bulma.io site and quickly realized that bulma did not have JS baked in, as bootstrap does have. The fix was on the bottom of the navbar documentation page, both a Vanilla JS and a JQuery snippet.

* Verdict:
JQuery code added to the scripts.js file worked like a charm and the navbar is now working as expected.

**Name** Flash messages not showing

* Bug description
The flash messages for log in and registration error handling weren't showing.

* Fix:
Forgot to put 
```     {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                <div class="columns">
                    <div class="column"></div>
                    <div class="column is-8">
                        <p class="flashes">
                        {{ message }}
                        </p>
                    </div>
                    <div class="column"></div>
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}
```
in the flash_messages file.

* Verdict:
Now working as expected.

**Name**

* Bug description

* Fix

* Verdict

**Name**

* Bug description

* Fix

* Verdict

## Deployment ##

### Local Deployment ###
I have created Story Chain using Github, from there I used Gitpod to write my code. Then I used commits to git followed by "git push" to my GitHub repository. I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku.

This project can be ran locally by following the following steps: ( I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

**To clone the project:**

    1. From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal:
       git clone https://github.com/byIlsa/story-chain.git
    2. Access the folder in your terminal window and install the application's required modules using the following command:
       pip3 install -r requirements.txt
    3. Sign-in or sign-up to MongoDB and create a new cluster
        ◦ Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called story_chain
        ◦ Set up the following collections: users, dogs, logs, food_metrics and weight Click here to see the exact Database Structure
          
        ◦ Under the Security Menu on the left, select Database Access.
        ◦ Add a new database user, and keep the credentials secure
        ◦ Within the Network Access option, add IP Address 0.0.0.0
    4. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. It will need to contain the following lines and variables:
       import os
       
       os.environ["IP"] = "0.0.0.0"
       os.environ["PORT"] = "5000"
       os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
       os.environ["DEBUG"] = "True"
       os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
       os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
       Please note that you will need to update the SECRET_KEY with your own secret key, as well as the MONGO_URI and MONGO_DBNAME variables with those provided by MongoDB. Tip for your SECRET_KEY, you can use a Password Generator in order to have a secure secret key. I personlly recommend a length of 24 characters and exclude Symbols. To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. Don't forget to update the necessary fields like password and database name.
       If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.
    5. The application can now be run locally. In your terminal, type the following command
       python3 app.py.

**To deploy your project on Heroku, use the following steps:**

    1. Login to your Heroku account and create a new app. Choose your region.
    2. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.

**Requirements:**

       pip3 freeze --local > requirements.txt

**Procfile:**

       echo web: python app.py > Procfile

    3. The Procfile should contain the following line:
       web: python app.py

**And then:**       

    4. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
    5. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
    6. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME): !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website.
       IP = 0.0.0.0
       PORT = 5000
       SECRET_KEY = YOUR_SECRET_KEY
       MONGO_URI = YOUR_MONGODB_URI
       MONGO_DBNAME = DATABASE_NAME
    7. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
    8. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
    9. In order to commit your changes to the branch, use git push to push your changes.

## Credit ##

Credits
    • Texts are all created by myself.

**Image credits**

* [Hero header image](https://pixabay.com/nl/photos/voorjaar-schrijven-communiceren-3237961/)
* [Error pages background](https://pixabay.com/nl/illustrations/briefpapier-canvas-afbeelding-670870/)

**Special thanks**
* My Yoda-mentor [Simen Daehlin](https://github.com/Eventyret) for being there when I lost my way and didn't know how to get back. And for being the kick-ass person that he is.
* [Anouk Smet](https://github.com/AnoukSmet), for her awesome README
* [SuzanneNL](https://github.com/SuzanneNL), for her project as a whole. Ive learned so much from just reading through your code, talking to you about it and from the way you've written your testing and bugs section really helped to understand what is going on.
* Everybody at Slack for their support, tips and humor! 

For his undying love and support and always being there, my love, you know who you are ;)

**Site for educational purposes only!**
