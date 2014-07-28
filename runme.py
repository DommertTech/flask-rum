from flask import Flask, render_template
from flask import Blueprint
from flask_rum.main import rum

app = Flask(__name__)
app.config.from_object('configs')
app.register_blueprint(rum)

@app.route('/fuckyou')
def fuckyou(title='fuck'):
    return 'Fuck you Cunt'

@rum.route('/suckit')
def frontpage(title='Home '):
    return render_template('site/frontpage.html', title=title)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)