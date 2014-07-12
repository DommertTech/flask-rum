Flask-Rum [Version 0.10.1]
==============
*Author:* Dommert [Dommert@Gmail.com]
*Published:* July 2014
*Updated:* July 2014


**Fill your Flask app with Rum!!**

Flask-Rum is a templating &amp; theme system built on top of Flask with Foundation and JQuery. Its a great starting point for any flask project.


Documentation & Website links will come soon.

### Getting Started
Have Python and VirtualEnv installed before this:

    git clone git@github.com:DommertTech/flask-rum.git
    cd flask-rum
    virtualenv ENV
    source ENV/bin/activate
    pip install -r requirements.txt
    python flask-rum/main.py
    open http://0.0.0.0:5000/


## Documentation

#### File Structure
* Main.py (of course the main file to run)
* Configs.py (your site configs and setups)
* templates/site (this is where you route your site pages and content)
* templates/rum/ (main layouts to expand upon)
    * Base.html (the base layout that everything is built upon)
    * Main.html (expands off the base, and is the main setup for body and things)
    * OneCol.html (expands off Main, setup with main content area)
    * TwoCol.html (expands off Main, has content area and sidebar)
    * Frontpage.html (expands off Main, your frontpage layout design)
* templates/coconut (a demo theme and a spice of coconut flavor to your Rum)
* static/js (all your Javascript libraries)
* static/rum/css (All of rums CSS files)

#### Rum Blocks Templates
These are the main block sections that make up Rum Templates. If you need help with Template look at Jinja2 Documentation.
* Title
* Rum_Head : Where you can add any extra CSS, JS, and Meta Data
* Rum_Header : The Top Section of Page
* Rum_Nav : Main Navigation Section
* Rum_Middle: Middle Section of Page
* Rum_Content : Main content section
* Rum_Sidebar : Sidebar for two/three columns
* Rum_Footer : Main footer section







