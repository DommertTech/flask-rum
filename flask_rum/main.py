# Dommert's Flask-Rum [Version 0.1.1]
# Fill your Flask with Rum!
from flask import Flask, render_template
from flask import Blueprint
import configs as settings

app = Flask(__name__)
app.config.from_object('configs')

rum = Blueprint('rum', __name__, template_folder='templates')
app.register_blueprint(rum)

@rum.route('/')
def frontpage(title='Home '+settings.PROJECT_TITLE):
    return render_template('site/frontpage.html', title=title)

@rum.route('/about/')
def about(title='About Us'):
    return render_template('site/about.html', title=title)

@rum.route('/info/')
def info(title='Info Page'):
    return render_template('site/info.html', title=title)

@rum.route('/<path:path>')
def catch_all(path, title='404 Error! '+settings.PROJECT_TITLE):
    return render_template('site/404.html', title=title, path=path)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
