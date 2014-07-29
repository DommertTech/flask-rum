# Dommert's Flask-Rum [Version 0.1.1]
# Dommert@Gmail.com
# Fill your Flask with Rum!! Aarrgghhh.....
from flask import Flask, render_template
from flask import Blueprint
import configs

app = Flask(__name__)
app.config.from_object('configs')

rum = Blueprint('rum', __name__, template_folder='rum_templates', static_folder='rum_static')
app.register_blueprint(rum)

@rum.route('/')
def frontpage(title='Home '+configs.PROJECT_TITLE):
    return render_template('site/frontpage.html', title=title)

@rum.route('/about/')
def about_index(title='About Us'):
    return render_template('site/about.html', title=title)

@rum.route('/info/')
def info_index(title='Info Page'):
    return render_template('site/info.html', title=title)

@rum.route('/<path:path>')
def catch_all(path, title='404 Error! '+configs.PROJECT_TITLE):
    return render_template('site/404.html', title=title, path=path)


