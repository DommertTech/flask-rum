# Dommert's Flask-Rum [Version 0.10.0]
# Fill your Flask with Rum!
from flask import Flask, render_template
from configs import *
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world(title='Hello World'):
    return render_template('rum/default.html', title=title, rum = rum)

@app.route('/about/')
def about(title='About Us'):
    return render_template('site/about.html', title=title, rum = rum)

@app.route('/testing/')
def testing(title='Test Page'):
    return render_template(rum['theme']+'testing.html', title=title, rum = rum)

@app.route('/one/')
def one_column(title='Test Page'):
    return render_template(rum['theme']+'onetest.html', title=title, rum = rum)

@app.route('/two/')
def two_column(title='Test Page'):
    return render_template(rum['theme']+'twotest.html', title=title, float="left;", rum = rum)

@app.route('/<path:path>')
def catch_all(path, title='Catch All'):
    return render_template(rum['theme']+'about.html', title=title, path=path, rum = rum)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
