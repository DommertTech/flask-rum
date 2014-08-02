# Dommert Flask-Rum Loader
from flask import Flask
from flask import render_template
from flask_rum.main import rum

app = Flask(__name__)
app.register_blueprint(rum)

import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
app.config.THEME_FOLDER='rum/coconut/'


@app.route('/sample')
def sample_pg(title='Home '):
    return render_template('site/frontpage2.html', title=title)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])