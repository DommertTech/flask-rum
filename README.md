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
* templates/rum/
** Base.html (the base layout that everything is built upon)
** Main.html (expands off the base, and is the main setup for body and things)
** OneCol.html (expands off Main, setup with main content area)
** TwoCol.html (expands off Main, has content area and sidebar)
** Frontpage.html (expands off Main, your frontpage layout design)
* templates/site (this is where you route your site content and themes)
* templates/coconut (a demo theme and a spice of coconut flavor to your Rum)
* static/js (all your Javascript libraries)
* static/rum/css (All of rums CSS files)

#### Info






