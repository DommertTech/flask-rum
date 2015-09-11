# Rum Example
# Author: Dommert (Dommert@Gmail.com)

# Dommert's Flask-Rum [Version 0.1.0]
# Fill your Flask with Rum!

from flask import Flask, render_template, Blueprint
from flask_rum import rum_config
from examples import my_config
from jinja2 import TemplateNotFound
from flask_rum.main import rum

app = Flask(__name__)
app.config.from_object(rum_config)

#rum = Blueprint('rum', __name__)
app.register_blueprint(rum)

@rum.route('/test1')
def info(title='Info Page'+rum_config.PROJECT_TITLE):
    return render_template('site/info.html', title=title)


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])