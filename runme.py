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

from rum import *


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])