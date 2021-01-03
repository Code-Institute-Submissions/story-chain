# Story Chain #
*So you think you can write?*

## Project goals ##
Writing stories can be a lot of fun. But what if you could write stories with complete strangers? In this app you can start a new story or add to an existing story. This way, you'll never know what is going to happen, making writing both more challenging and fun!

## UX ##
### User Goals ###
* The website has to work well on all kind of devices like mobile phones, tables and desktops 
* The login procedure should be clear and feedback should be given when appropriate
* The registration process should be clear, easy to do and feedback should be given when appropriate
* The website has to be easy to use and easy to update information 
* Visually appealing website 

### User Stories ###
* As a user, I would like to be able to register for the website so I can have my personal environment. 
* As a user, I want to login after I created an account and see my previous inserted information. 
* As a user, I would like to have a personal environment (profile page) where I can see everything I have posted. 
* As a user, I want to be able to add a new story.
* As a user, I want to be able to add content to an existing story. 
* As a user, I want to be able to edit the new story or the content I have added to an existing story. 
* As a user, I want to be able to delete the stories I have started or contributed to.
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

![Color scheme](/assets/wireframes/colorscheme.png)

* #F8F8FF: This is a more off white color, to keep the more darker toned colors together and create a more warming atmosphere. This will be the background color.
* #000000: This will be the main font color. 
* #BC5609: This will be the font color for the logo and the titles on the homepage.
* 5F2121: This will be the color of the lines and borders.

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

You can find my wireframes below:

**Desktop Wireframes:**

**Tablet Wireframes:**|

**Mobile Wireframes:**

### Flowcharts ###
I have decided to make a flowchart for the sign-in / register / delete account / change username and/or password process to completely understand each step of the process.

I have used !!!!! to make this flowchart which you can view below:

![Flowchart]()

### Data Models ###
I also created a conceptual data model to get a feel for the needed entities, relationships and attributes, which have also helped me form the user stories.

![Conceptual Data Model]()

#### Database Structure ####
For this project I have used [MongoDB](https://www.mongodb.com/cloud/atlas) with the following collections:

## Features ##

### Features that are implemented ###
* Registration functionality 
* Sign-In and Out functionality 
* Add a new story
* Add to an existing story
    * CRUD Functions: 
        * Create: possibility to create a new story
        * Read: home page with stories in progress that non-members can also read, as well as a profile page where members can see what the have added.
        * Update: possibility to edit the content that a member has added and change username and/or password.
        * Delete: possibility to delete content that a member has added and delete account.

### Features to be implemented ###
* Have a 'forget password' functionality
* Add a search functionality 

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

## Testing ##
***Registration***

**User story: As a user, I would like to be able to register for the website so I can have my personal environment**

* Plan

* Implementation

* Test

* Result

    * Verdict The test has passed all the criteria and works like planned.

***Sign In***

**User story: As a user, I want to login after I created an account and see my previous inserted information.**

* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Profile Page***

**User story: As a user, I would like to have a personal environment (profile page) where I can see everything I have posted.**

* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Add content***

**User story: As a user, I want to be able to add a new story.**

* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

**User story: As a user, I want to be able to add content to an existing story.** 
* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Edit new and/or existing story***

**User story: As a user, I want to be able to edit the new story or the content I have added to an existing story.** 
* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Delete added content by member***

**User story: As a user, I want to be able to delete the stories I have started or contributed to.**
* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Account options***

**User story: As a user, I want to be able to change my username and password.**

* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

**User story: As a user, I want to be able to delete my account.**

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

***Log out***
**User story: As a user, I want to be able to log out of my profile.**

* Plan

* Implementation

* Test

* Result

    * Verdict: The test has passed all the criteria and works like planned.

## Bugs ##

**Name**

* Bug description

* Fix

* Verdict

**Name**

* Bug description

* Fix

* Verdict

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

### Deployment to Heroku ###

## Credit ##


