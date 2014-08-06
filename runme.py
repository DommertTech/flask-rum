# Flask-Rum [Version 0.1.2]
# Dommert Flask-Rum Loader

from flask import Flask
from flask import render_template
app = Flask(__name__)



# Sample Override over route('/about/')
@app.route('/about/')
def about2(title='Home '):
    return render_template('site/sample.html', title=title)

# Regular Route using Flask-Rum
@app.route('/sample')
def sample(title='Home '):
    return render_template('site/sample.html', title=title)


# ---- RUM ----------------------------
from flask_rum.main import rum
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
# Sample override of Theme
app.config.THEME_FOLDER='rum/banana/' # Flavor of Rum
app.register_blueprint(rum) #  Flask-Rum Blueprint

#------------------------------------

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])