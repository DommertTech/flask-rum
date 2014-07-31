# Dommert Flask-Rum Loader
from flask import Flask, render_template
from flask_rum.main import rum

app = Flask(__name__)
app.register_blueprint(rum)
app.config.update(
    DEBUG=True,
    #SECRET_KEY='...',
    THEME_FOLDER='rum/banana/',
    TEMPLATE_DEFAULTS = {
    'nav': 'site/blocks/rum_nav.html',
    'footer': 'site/blocks/rum_footer.html'
    }
)

@app.route('/fuckyou')
def fuckyou(title='fuck'):
    return 'Fuck you Cunt'

@app.route('/suckit')
def suckit(title='Home '):
    return render_template('site/frontpage2.html', title=title)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)