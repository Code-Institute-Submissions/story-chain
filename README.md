# Story Chain #

*So you think you can write?*

![Header Image](/static/images/hero-header.jpg)

- [Project goals](#project-goals)
- [UX](#ux)
  - [User Goals](#user-goals)
  - [Scope](#scope)
- [Structure of the website](#structure-of-the-website)
  - [View for a guest user](#view-for-a-guest-user)
  - [View for logged in user](#view-for-logged-in-user)
  - [User Stories](#user-stories)
  - [Site owner goals](#site-owner-goals)
- [User Requirements and Expectations](#user-requirements-and-expectations)
  - [Requirements](#requirements)
  - [Expectations](#expectations)
- [Design Choices](#design-choices)
  - [When and why i've diverted from the wireframes](#when-and-why-i've-diverted-from-the-wireframes)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Icons](#icons)
  - [Structure](#structure)
- [Wireframes, Flowcharts and Data Models](#wireframes--flowcharts-and-data-models)
  - [Wireframes](#wireframes)
  - [Flowcharts](#flowcharts)
  - [Data Models](#data-models)
    - [Database Structure](#database-structure)
- [Features](#features)
  - [Features that are implemented](#features-that-are-implemented)
  - [The Big Struggle](#the-big-struggle)
  - [Features to be implemented](#features-to-be-implemented)
  - [Known issues](#known-issues)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools](#tools)
- [Testing](#testing)
  - [Testing user stories](#testing-user-stories)
- [Manual testing](#manual-testing)
  - [From validating](#from-validating)
- [Bugs](#bugs)
  - [In development](#in-development)
  - [From peer code review](#from-peer-code-review)
  - [From friends and family testing](#from-friends-and-family-testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
- [Credit](#credit)
  - [Image credits](#image-credits)
  - [Special thanks](#special-thanks)

## Project goals ##

Writing stories can be a lot of fun. But what if you could write stories with complete strangers? In this app you can start a new story or add to an existing story.
This way, you'll never know what is going to happen, making writing both more challenging and fun!

## UX ##

### User Goals ###

- The website has to work well on all kind of devices like mobile phones, tables and desktops
- The login procedure should be clear and feedback should be given when appropriate
- The registration process should be clear, easy to do and feedback should be given when appropriate
- The website has to be easy to use and easy to update information
- Visually appealing website

### Scope ###

An easy to navigate and responsive website that is fun to use and allows users to perform CRUD operations. Users can sign up and, once logged in, share their stories. These users manage their own stories, meaning they can edit and delete them when they want.
Also, they can update their password and username and even delete their account.

## Structure of the website ##

### View for a guest user ###

A user that is not logged in and/or registered, will see a list of all stories on the homepage. There is also a call to action button 'Join Us!' urging them to register. They also have a navigation menu, only containing 'Home', 'Register' and 'Log In'.
All other functionality is restricted to a logged in user.
They are able to click the 'Read More' button in the story card, which will lead them to the 'Read Story' page. Here they are also prompted to register/login to benefit from the full functionality of the site.

### View for logged in user ###

A logged in user will benefit from the full functionality of the site. The navigation will contain: 'Home', 'Profile (with their username for ease)', 'Add' and 'Logout'.
This user can then add a new story by clicking the 'Add' button in the navigation or on their profile.
The added functionality for this user is the ability to add a story, edit that story and even delete is. This functionality is restricted for only to the user that is logged in and is also the creator of that story.
In the profile there are also functions for changing once username, password and even delete their account. The can also add a 'chain' to content created by a different user.
All this added functionality is also available to the site owner via an "admin" account.

### User Stories ###

- As a user, I would like to be able to register for the website so I can have my personal environment.
- As a user, I want to login after I created an account and see my previous inserted information.
- As a user, I would like to have a personal environment (profile page) where I can see everything I have posted.
- As a user, I want to be able to add a new story.
- As a user, I want to be able to add content to an existing story.
- As a user, I want to be able to edit the new story or the content I have added to an existing story.
- As a user, I want the website to be easy to use.
- As a user, I want the process to add / edit / delete info to be easy.
- As a user, I want to be able to logout of my profile.
- As a user, I want to be able to change my username and password.
- As a user, I want to be able to delete my account.

### Site owner goals ###

- To have an appealing website that enables people to write stories.
- To have a great functionality so the user feels like this website enables them to practice writing or just enjoy reading what other user have wrote.
- To make the website more personal, by having everything the user has written, be on display on their profile page.

## User Requirements and Expectations ##

### Requirements ###

- Easy to navigate by using buttons
- Appealing profile page with a functional overview
- Easy way to add a a new story
- Easy way to add onto an existing story
- Ability to edit and delete any entries

### Expectations ###

- When you have multiple stories, it should be easy to decern them and edit or delete them when necessary.
- To have a profile page where all the necessary information is visible.
- It should be easy to add a new story or add onto an existing story.

## Design Choices ##

I have based the designs for this website on the image used for the hero header. I wanted to create an atmosphere of warmth and welcome any user to join the fun.

### When and why i've diverted from the wireframes ###

For the homepage I had originally decided on a 3-by-3 card system (for larger screen views). But when implementing this, I really didn't like the look of it. So I decided to add the stories to the homepage as it is now. I also changed the text color of the buttons to white,
so it would be easier to read (contrast). I also did not implement the 'add chain' on the same page as the story, because I felt this became to busy with the buttons and all.
The profile styling was simplified, as there isn't much functionality as is now, to justify diverting from the overall styling of the site. The log in form on the wireframes has one password field. For simplicity sake and as an extra security measure, i've decided to keep
the second password field from the register form.

### Colors ###

I have used [Coolors](https://coolors.co/) for creating a color scheme.

![Color scheme](/readmecontent/images/colorscheme.jpg)

- #F8F8FF: This is a more off white color, to keep the more darker toned colors together and create a more warming atmosphere. This will be the background color.
- #000000: This will be the main font color.
- #BC5609: This will be the color of the lines and borders.
- 5F2121: This will be the font color for the logo and the titles on the homepage.

I have used a contrast checker in order to make sure that the contrast is sufficient. This way my content will be easily readable.

### Fonts ###

The fonts I’ll be using are:

[Indie Flower:](https://fonts.google.com/specimen/Indie+Flower?query=Indie) For the logo, header and titles

[Raleway:](https://fonts.google.com/specimen/Raleway?query=raleway) For the content

Fonts are from [Google Fonts.](https://fonts.google.com/)

### Icons ###

Icons used are from [Font Awesome.](https://fontawesome.com/) The are used in moderation and match the colors and overall feel of the design.

### Structure ###

For the structure I have used [Bulma.](https://bulma.io/) I wanted to challenge myself to not use Bootstrap (as I have done in former projects) or Materialize,
but found it important (and fun!) to use something completely different.

## Wireframes, Flowcharts and Data Models ##

### Wireframes ###

For wireframing I have used [Pencil.](https://pencil.evolus.vn/)

View my wireframes [here](https://github.com/byIlsa/story-chain/blob/master/wireframes/wireframes.pdf).

### Flowcharts ###

I have decided to make a flowchart for the sign-in / register process to better understand each step of the process.

You can view this below:

![Flowchart](/readmecontent/images/flowchart.jpg)

### Data Models ###

I also created a conceptual data model to get a feel for the needed entities, relationships and attributes, which have also helped me form the user stories.

![Conceptual Data Model](/readmecontent/images/conceptualdatamodel.jpg)

#### Database Structure ####

For this project I have used [MongoDB](https://www.mongodb.com/cloud/atlas).It contains three collection, 'users', 'stories' and 'chains'. When a user registers, his username and hashed password are added to the users collection.
When a logged in user adds a story to the website, his username is added as a value for the key 'author' in the stories collection. When a user adds a chain, the chain id is passed into the 'story_chains' array in the
stories collection, as well as the username from the users collection, as author.

A more accurate Data model can be viewed here:

![dbdiagram](/readmecontent/images/storychain.jpg)

## Features ##

### Features that are implemented ###

- Registration functionality
- Log In and Out functionality
- Add a new story
- Add to an existing story (See ["The big struggle"](#the-big-struggle))
- CRUD Functions:
  - Create: possibility to create a new story and add to an existing story.
  - Read: home page with stories that non-members can also read, as well as a profile page where members can see what the have added.
  - Update: possibility to edit the content that a member has added and change username and/or password.
  - Delete: possibility to delete content that a member has added and delete account.

### The Big Struggle ###

As might be clear now, the whole 'add to an existing story' has been quit a challenge. But, what is important, is that the function itself has been implemented, a few days shy from the project deadline.
I also, with some help from my mentor, was able to not have all chains being removed if a user changed the original story.

I could  not let this one go. It toke two tutors (Johann and Miklos) and a very patient fellow student [Karina](https://github.com/kairosity) who have been an instrumental help to getting
this function up and running!

My eternal thanks go out to them for this one.

### Features to be implemented ###

- Have a 'forget password' functionality
  - The user now has the ability to change their email. But I would really like to have a 'forgot your password' function so a user can reset it.
- Add a search functionality
  - To allow a search functionality I am thinking about having people include 'tag' words so other users could search by matching those keywords.
- A way to add the username 'guest' to stories from people who have deleted their account without them deleting their stories.
  - The way it is right now, a new user is technically able to register that username again and own those stories.

### Known issues ###

- When a user changes his username, all the content he has added, is no longer accessible by the new username.
- When a user deletes his account without removing their content first, a new user that picks the username of the account that has been deleted, gets access to that content.
- When a user has successfully submitted a form, he is redirected. But when the user clicks the 'back' button on the browser, the form is back with the information that has already been submitted.
He can then submit again (and a malicious script can overload the site and cause many issues.

## Technologies used ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JS](https://nl.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Frameworks ###

- [Font Awesome](https://fontawesome.com/)
- [Bulma](https://bulma.io/)
- [Google Fonts](https://fonts.google.com/)
- [jQuery](https://jquery.com/)

### Tools ###

- [Git](https://git-scm.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [Pencil](https://pencil.evolus.vn/)
- [PEP8](http://pep8online.com/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [MongoDB Atlas](https://www.mongodb.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Heroku](https://www.heroku.com/)
- [Github](https://github.com/)
- [Chromium](https://www.chromium.org/Home)

## Testing ##

The site was tested by using the LightHouse function for Chromium Developer Tools. A report can be found [here](/readmecontent/images/storychainlighthousetest.pdf)

### Testing user stories ###

***Registration***

User story: As a user, I would like to be able to register for the website so I can have my personal environment

- A reddish call to action button in the hero image with the text "Join Us!" is presented. There is also a ‘register’ link in the navigation bar at the top.
When users want to register, they only have to provide a username and password.
After registering, they will be redirected to their profile page. There they see an section with an 'add' button at the top of the screen as well as a ‘account options’ section for editing the username and/or password and deleting their account.
On this page all stories they have started are also displayed. At all stages where a user input is given, flash messages direct the user if an action was indeed successful or explain what went wrong.

- All is working as intended.

***Sign In***

User story: As a user, I want to login after I created an account and see my previous inserted information.

- A user can log in by clicking the 'Log In' button in the navigation.
He is then directed to a login form, that prompts for the username and password.
After the login is successful, the user is redirected to their profile, where an appropriate flash message is given.
On the profile, when applicable, any content that is submitted by the user, is presented.
Also the ability to change their username, password and delete account is given.

- All is working as intended.

***Profile Page***

User story: As a user, I would like to have a personal environment (profile page) where I can see everything I have posted.

- After a user has had a successful login or registration, he is redirected to his personal profile page.
Here he can see any previous started stories and have full account control by having the ability to change a username, change a password and delete his account.
Also a section for 'add' a story is given.

- All is working as intended.

***Add new story***

User story: As a user, I want to be able to add a new story.

- After an user is logged in, an 'Add' button appears in the navigation, as well as in their profile.
This will prompt a form for them to fill. After a successful submit action, the story will be displayed on both the home page as well as their profile page.
Before hitting submit, the user also has an option to cancel the action by clicking the 'cancel' button.
Appropriate feedback is given by flash messages after clicking the 'submit' button.

- All is working as intended.

***Edit an existing story***

User story: As a user, I want to be able to edit the new story.

- A user that is the writer of a story will have buttons presented under that content that allows them to edit it.
This is only visible if the logged in user also matches the user that has submitted the content.
A pre filled form is given to be edited and after a successful submission, the user is redirected to the home page and presented with an appropriate flash message.
There is also a button that let's the user cancel it's action and return to the home page if he should so desire.

- All is working as intended.

***Delete story***

User story: As a user, I want to be able to delete the stories I have started.

- After clicking the 'Read More' button in a story from the home page and if the current user is also the author of the story, a 'edit' and a 'delete' button will appear.
After the user clicks the 'delete' button, it will prompt a modal, warning the user that deleting the content seriously affects the flow of the story.
A user can then either click a 'cancel' button which will close the modal or click 'delete' once more. This will then delete the story from the database, homepage and the profile.
An appropriate flash message will be given.

***Creating, editing and deleting content to an existing story***

User story: As a user, I want to be able to add content to a existing story.

- When a logged in user is on the 'Read More' page, an 'Add Chain' button is presented, which leads to a form that enables the user to add chain. On successful submit,
the user is redirected to the 'Read Story' page where the chain is added.

- All is working as intended.

User story: As a user, I want to be able to edit/delete content to an existing story.

- Not yet implemented, still working on this user story.

***Account options***

User story: As a user, I want to be able to change my username and password.

- After a user has had an successful login, he is directed to his profile page. There they see three buttons 'Change username', 'Change password' and 'Delete account'.
The 'change username' button opens a small form that asks the user to enter a new username.

This username is then checked against existing usernames in the database and gives appropriate feedback. The old user is logged out and is asked to log in with the new username.
Unfortunately, all content added by this user under his old username, will no longer be accessible with the new username. This needs a fix.
See [Known issues](#known-issues)

- After a user has had an successful login, he is directed to his profile page. There he can click the 'Change password' button.
He is then led to a small form, asking for a new password. That password is then hashed and stored in the database.

User story: As a user, I want to be able to delete my account.

- After a user has had an successful login, he is directed to his profile page. There he can click the 'Delete account' button.
A modal pops up, asking the user he is sure about deleting their account. After clicking "I'm sure", their account is deleted from the database. If a new user picks the username of the user that has
deleted their account, all that content by that username is now accessible for that new user. This needs a fix. See [Known issues](#known-issues)

***Log out***

User story: As a user, I want to be able to log out of my profile.

- Once a user is logged in, in the navigation, a button appears that has the text 'Log Out' on it.
Once clicked, the user is logged out and returned to the homepage. An appropriate flash message will be displayed.

- All is working as intended.

## Manual testing ##

All manual testing was done using Chromium Developer Tools and testing on an iPhone 11 and an iPad Pro.

Home

- On the homepage, all stories are displayed in cards, only showing the title, the author, the date they where posted and a small portion of the text and a 'Read More' link.

Register

- Before signing up, users see the options Home, Register and Log In in the navigation bar.
- In the Register form: provide username of more than 2 and less then 15 characters. The form tells a user that the username doesn't meet the criteria (validation message). A help message has been displayed beneath the form field stating: "Only letters (either case) and numbers. No special characters"
- Provide a password of more than 5 and less then 15 characters. The form tells a user that the password doesn't meet the criteria (validation message). A help message has been displayed beneath the form field stating: "Only letters (either case) and numbers, 6 or more characters".
- Leave one or more fields empty. The form tells a user that the empty field needs to be filled in (validation message).
- Provide username or password containing forbidden characters. Only a-z, A-Z, and 0-9 are allowed. The form tells a user that the username or password don't meet the criteria (validation message).
- Provide a username that already exists and submit the form. The user is redirected back to the sign up page. A flash message is visible: 'Username already taken.'
- Provide a username and password that meet the criteria, the user is added to the 'users' collection in the database and redirected to their profile page.  On the website, the user sees the options Home, Profile, Add and Log Out in the navigation bar.

Log In

- Click the 'Log in" button in the navigation menu. The user is lead to a log in form. Same rules apply as the register form.
- After a successful login, the user is redirected to their profile page.

Read Story

- When clicking on the Read More link on a story on the home page, a new page opens and the full story (with chains if there are some) can be read.
- If the user is also the author of the story, a 'edit' and 'delete' button appears. If the user is not the author, these buttons do not show.
- If the 'edit' button is clicked, a form opens up, that allows the author to edit both the title and the content. Both fields need to be filled. When the 'edit story' button is clicked, an appropriate flash message is shown and the user is
redirected to the 'Read Story' page.
- When the 'delete' button is clicked, a modal is triggered, where the user is made aware that this process cannot be undone and asked to click 'delete' again. There is also a 'cancel' button which closes the modal and no action is taken.
- An 'Add Chain' button is presented to everyone who is logged in.
- A 'Home' button is presented to avoid using the back button of the browser.

Add story

- When an user is logged in, an 'Add' button appears in both the navigation and their personal profile. When clicked, a form opens, allowing for a story to be started. A title and some content is required and if this is not added correctly, the form will not be submitted.
A help text will be displayed, giving information about why submitting isn't allowed at that stage. When the submit is successful, an appropriate success flash message is displayed and the user is redirected to the home page, where the story is displayed.

Profile

- When an user has logged in, he is redirected to his profile. On this personal page, the user has a couple of options. There is the ability to change the username, change the password and delete their account (see 'Known issues').
- There is also an extra call to action button to add a new story and there is a space where the submitted stories of that user are being displayed (also has a 'Read More' link that leads to the 'Read Story' page and gives extra options for editing and deleting this content).

Errors

- Four custom error pages where added to handle the most common http errors (404, 401, 500 and 405).

### From validating ###

- Python code has been validated for pep8 compliance with [pep8 validator](http://pep8online.com/) and gave no errors. [result](./readmecontent/images/pep8.jpg)

- HTML code has been validated with [HTML validator](https://validator.w3.org/nu/) and gave no errors. [result](./readmecontent/images/htmlvalidator.jpg)

- CSS code has been validated with [CSS validator](https://jigsaw.w3.org/css-validator/). For the style.css file there where no errors.
I did get a lot of errors that where linked to the css files from Bulma (in the CDN). [result](./readmecontent/images/cssvalidator.jpg)

- JS code has been run through [Esprima](https://esprima.org/index.html) which gave no errors. [result](/readmecontent/images/esprima.jpg)

## Bugs ##

### In development ###

Navbar collapse not working

- Bug description:
  - After finishing the basic and extended navbar, I quickly noticed that the hamburger menu wasn't behaving as expected.

- Fix:
  - I looked on the bulma.io site and quickly realized that bulma did not have JS baked in, as bootstrap does have. The fix was on the bottom of the navbar documentation page, both a Vanilla JS and a JQuery snippet.

- Verdict:
  - JQuery code added to the scripts.js file worked like a charm and the navbar is now working as expected.

Flash messages not showing

- Bug description:

  - The flash messages for log in and registration error handling weren't showing.

    - Fix:
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

    - Verdict: Now working as expected.

Register and Login form not centering

- Bug description:

  - Register form and login form did not center both, although seemingly, they were both on the same CSS and HTML because of the templating. Originally I used empty columns to center
the column(s) with the content. Where this worked for the most part, it didn't in this instance.

- Fix:
  - The fix wasn't all that difficult. Don't use empty columns as it tends to get messy when there is more content. A fellow student pointed out to me Bulma had this amazing thing called flexbox :)
Ditch the empty columns and use 'is-centered' on the ```<div class="columns is-centered"></div>``` and give the column with the content an ```<div class="column is-half"></div>``` and the problem is solved.

- Verdict:
  - Solved! Nice and centered. Like it should be :)

Modals for delete functions not working as expected

- Bug description:

  - I wanted to have two modals that gave some extra security on the delete story and delete account function. I build the modals and wired them up,
    to discover that the JS couldn't discern correctly between the two. Also, me thinking about the DRY principal, didn't feel for building two
    separate, yet similar functions so I went on an online search.

- Fix:
  - The fix came from the almighty Stack Overflow( see script.js for credit). I now have two modals wired up with four lines of code :)

    ``` $(".button").click(function(){
        $(".modal").removeClass("is-active");
        var Type = $(this).data("modal-type");
        $("#"+Type).addClass("is-active");
    ```

- Verdict:
  - All good!

Buttons not responsive

- Bug description:

  - All buttons where not responsive, making them look very big on smaller screens.  Bulma is a very 'basic' framework, allowing you to customize it. Downside is that you might overlook certain things
    that are built in in say Bootstrap. For me, this was one of them.  

- Fix:
  - The fix came from the almighty [Stack Overflow](https://stackoverflow.com/questions/54371733/responsive-buttons-and-spacing-helpers)

    ``` @media screen and (max-width: 768px) {
            .button.is-small-mobile {
            font-size: 1.75rem;
            border-radius: 290486px;
            padding-left: calc(1em + .25em);
            padding-right: calc(1em + .25em);
        }
    }
    ```

- Verdict:
  - All good!

### From peer code review ###

'About' content being a bit squished when centered.

- Bug description:
  - Especially on mobile devices the about content on the homepage got squished.

- Fix:
  - I added some padding to the list items to move them apart a bit more.

- Verdict:
  - All good.

Burger menu icon push to right on mobile

- Bug description:
  - On mobile devices the burger menu icon was pushed a bit to far to the right side of the screen.

- Fix:
  - Added some margin to the burger menu icon.

- Verdict:
  - Now working as expected.

Textarea field of add chain had overflow

- Bug description:
  - On mobile devices, the textarea field had some overflow.

- Fix:
  - Gave the field some more margin to the right and removed overflow-x: hidden.

- Verdict:
  - Behaves better now

### From friends and family testing ###

There weren't bugs from them per se, but more some things they would like to see.

Implemented:

- Want:
  - Time added to the date on the story cards so the time of posting (and order of posting and linking) becomes more obvious.
    - Added time to the app route and new stories and content now show the time of posting, next to the date.

Feature implements:

- Want:
  - When someone adds a chain and someone else also does this, the flow might become distorted because of some 'double posting'.
    - I want to figure out a way that I can maybe 'lock' the add function if someone is already started a new chain.

- Want:
  - A way to get notified when someone has added something.
    - This would require the email-address being added to the register function and find a way to build a notification function.

## Deployment ##

### Local Deployment ###

I have created Story Chain using Github, from there I used Gitpod to write my code. Then I used commits to git followed by "git push" to my GitHub repository.
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku.

This project can be ran locally by following the following steps: ( I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE.
You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

**To clone the project:**

- From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal:
    git clone ``https://github.com/byIlsa/story-chain.git``

- Access the folder in your terminal window and install the application's required modules using the following command:
    pip3 install -r requirements.txt

- Sign-in or sign-up to MongoDB and create a new cluster

    ◦ Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called story_chain

    ◦ Set up the following collections: users, stories and chains. Click [here](#database-structure) to see the exact Database Structure

    ◦ Under the Security Menu on the left, select Database Access.

    ◦ Add a new database user, and keep the credentials secure

    ◦ Within the Network Access option, add IP Address 0.0.0.0

- In your IDE, create a file containing your environmental variables called env.py at the root level of the application. It will need to contain the following lines and variables:
    import os

    ``` os.environ["IP"] = "0.0.0.0"
        os.environ["PORT"] = "5000"
        os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
        os.environ["DEBUG"] = "True"
        os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
        os.environ["MONGO_DBNAME"]= "DATABASE_NAME"
    ```

    Please note that you will need to update the SECRET_KEY with your own secret key, as well as the MONGO_URI and MONGO_DBNAME variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a Password Generator in order to have a secure secret key. I personally recommend a length of 24 characters and exclude symbols.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. Don't forget to update the necessary fields like password and database name.
    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

- The application can now be run locally. In your terminal, type the following command
    python3 app.py.

**To deploy your project on Heroku, use the following steps:**

- Login to your Heroku account and create a new app. Choose your region.
- Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.

**Requirements:**

``` pip3 freeze --local > requirements.txt ```

**Procfile:**

``` echo web: python app.py > Procfile ```

- The Procfile should contain the following line:

``` web: python app.py ```

**And then:**

- Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.

- From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.

  - Scroll back up and click "settings".
    - Scroll down and click "Reveal config vars".
    - Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME): !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website.

    ``` IP = 0.0.0.0
        PORT = 5000
        SECRET_KEY = YOUR_SECRET_KEY
        MONGO_URI = YOUR_MONGODB_URI
        MONGO_DBNAME = DATABASE_NAME
    ```

- Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
- Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
- In order to commit your changes to the branch, use git push to push your changes.

## Credit ##

Credits
    • Texts are all created by myself or the user who submitted it.

### Image credits ###

- [Hero header image](https://pixabay.com/nl/photos/voorjaar-schrijven-communiceren-3237961/)
- [Error pages background](https://pixabay.com/nl/illustrations/briefpapier-canvas-afbeelding-670870/)

### Special thanks ###

- My Yoda-mentor [Simen Daehlin](https://github.com/Eventyret) for being there when I lost my way and didn't know how to get back. And for being the kick-ass person that he is.
- [Anouk Smet](https://github.com/AnoukSmet), for her awesome README
- [SuzanneNL](https://github.com/SuzanneNL), for her project as a whole. Ive learned so much from just reading through your code,
talking to you about it and from the way you've written your testing and bugs section really helped to understand what is going on.
- [Karina](https://github.com/kairosity) for helping me navigating the templating stuff and help me get the add chain function up and running.
- Johann, Miklos from Tutor support for helping me getting the add chain function up and running and Tim from tutor support for helping me sort out a templating inheritance issue.
- Everybody at Slack for their support, tips and humor!

For his undying love and support and always being there, my love, you know who you are ;)

**Site for educational purposes only!**
