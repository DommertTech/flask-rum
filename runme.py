# Dommert Flask-Rum Loader
from flask import Flask
from flask import render_template
app = Flask(__name__)

#Import in Rum Configs
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)

# Sample override of Theme
app.config.THEME_FOLDER='rum/coconut/'

# Sample Override over route('/about/')
@app.route('/about/')
def about2(title='Home '):
    return render_template('site/frontpage2.html', title=title)

#  Flask-Rum Blueprint
from flask_rum.main import rum
app.register_blueprint(rum)

# Regular Route using Flask-Rum
@app.route('/sample')
def sample(title='Home '):
    return render_template('site/frontpage2.html', title=title)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])