Flask-Rum [Version 0.1.2]
==============
*Author:* Dommert [Dommert@Gmail.com] 
Facebook: http://facebook.com/dommertbot
Twitter: http://twitter.com/dommert
*Published:* July 4, 2014
*Updated:* December 7, 2014


## **Fill your Flask app with Rum!!**

Flask-Rum is a Flask Blueprint using Zurb's Foundation, JavaScript, and JQuery. It makes a great starting point, or extension, for any project or website. Flask-Rum comes with base website layouts, sections, blocks, and themes. You can use the base Themes out the box, or create your own. Flask Rum's default layouts are one column, two column with side bar floating on either left or right side, and three column layout. 

#### Notes
Version 0.1.0: Main Working app, getting ready for PyPi
Version 0.0.3: Working on making it modular and submitting it to PyPi. 
Version 0.0.2: Also turned Flask-Rum into a blueprint. Now you can add it into any project :)  
Version 0.0.1: I've started building on the Git-Wiki. Documentation & Website links will come soon.

## Documentation
Working on writing more documentation. I have started the Github wiki for the project. 

Zurb Foundation can be found here http://foundation.zurb.com/


### Basics!
**Every THEME has LAYOUT pages. Each Layout is divided into SECTIONS. Each Section can have BLOCKS.**

Every *theme* must come with these *layouts*! 
* frontpage
* onecol
* twocol
    
Each *layout* has these default *sections*
* Header
* Nav
* Content
* Footer


#### Rum Sections & Blocks
These are the main blocks and sections that make up Rum Templates. If you need help with Template look at the Jinja2 Documentation.
Each template requires Rum_Nav & Rum_Content

Sections & Blocks
*italic* = html tags

* *[Head]*
    * Title
    * Rum_Head : Where you can add any extra CSS, JS, and Meta Data
* *[Body]*
* *[Header]*
    * Rum_Header : The Top Section of Page
    * Rum_Nav : Main Navigation Section
* *[section id='middle']*
    * Rum_Middle: Middle Section of Page
    * Rum_Content : Main content section
    * Rum_Sidebar : Sidebar for two/three columns
* *[Footer]*
    * Rum_Footer : Main footer section



#### File Structure (need to update for v0.1.2)
* *Main.py* (Main Blueprint)
* *Rum_Config.py* (Default Rum Configurations)
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



