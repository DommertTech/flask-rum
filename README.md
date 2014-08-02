Flask-Rum [Version 0.1.2]
==============
*Author:* Dommert [Dommert@Gmail.com]
*Published:* July 4, 2014
*Updated:* August 1, 2014


## **Fill your Flask app with Rum!!**

Flask-Rum is a Flask Blueprint using Zurb's Foundation, JavaScript, and JQuery. It makes a great starting point, or extension, for any project or website. Flask-Rum comes with base layouts, blocks, sections and themes. 

#### Notes
Version 0.1.2: Turned Flask-Rum into a blueprint. Now you can add it into any project :)  
Version 0.1.1: I've started building on the Git-Wiki. Documentation & Website links will come soon.

### Getting Started
Have Python and VirtualEnv installed before this:

    git clone git@github.com:DommertTech/flask-rum.git
    cd flask-rum
    virtualenv ENV
    source ENV/bin/activate
    pip install -r requirements.txt
    python flask-rum/main.py
    open http://0.0.0.0:5000/
    or http://localhost:5000/


## Documentation

#### File Structure (need to update for v0.1.2)
* *Main.py* (Main Blueprint)
* *Rum_Config.py* (Rum Configurations)
* *rum_templates/*
    * *site/* (Route your site Pages and content)
        * Blocks/ (for custom site blocks)  
            * Defaults: rum_nav, rum_footer
    * *rum/core/* (main layouts to expand upon)
        * Base.html (the base layout that everything is built upon)
        * Main.html (expands off the base, and is the main setup for body and things)
        * OneCol.html (expands off Main, setup with main content area)
        * TwoCol.html (expands off Main, has content area and sidebar)
        * Frontpage.html (expands off Main, your frontpage layout design)
    * *rum/coconut/* (Simple Coconut Flavor Theme to add to your Rum)
    * *rum/banana/* (Yummy Banana Theme for Rum)
* *rum_static/* (your rum static files)
    * js/ (Javascript libraries)
        * JQuery/ (Jquery Library)
        * Foundation/ (Foundation Library)
        * Vender/
            * Modernizer.JS
            * PlaceHolder.JS
            * FastClick.JS
    * *rum/css* (base rum css files)
    * *[THEME_FOLDER]* (theme CSS & Files)


#### Rum Blocks
These are the main blocks and sections that make up Rum Templates. If you need help with Template look at Jinja2 Documentation.
Each template requires Rum_Nav and Rum_Content

*italic* = html
* *[head]*
* Title
* Rum_Head : Where you can add any extra CSS, JS, and Meta Data
    * *[body]*
    * *[header]*
* Rum_Header : The Top Section of Page
* Rum_Nav : Main Navigation Section
    * *[section id='middle']*
* Rum_Middle: Middle Section of Page
* Rum_Content : Main content section
* Rum_Sidebar : Sidebar for two/three columns
    * *[footer]*
* Rum_Footer : Main footer section







