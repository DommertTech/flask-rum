# Dommert's Flask-Rum [Version 0.1.1]
# Fill your Flask with Rum!
from flask import Flask, render_template
from configs import *
app = Flask(__name__)
app.debug = True


@app.route('/')
def frontpage(title='Home '+rum['title']):
    return render_template('site/frontpage.html', title=title, rum = rum)

@app.route('/about/')
def about(title='About Us'):
    return render_template('site/about.html', title=title, rum = rum)

@app.route('/info/')
def info(title='Info Page'):
    return render_template('site/info.html', title=title, rum = rum)

@app.route('/<path:path>')
def catch_all(path, title='404 Error! '+rum['title']):
    return render_template('site/404.html', title=title, path=path, rum = rum)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

