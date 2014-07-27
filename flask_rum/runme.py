from flask import Flask, render_template
from main import rum

app = Flask(__name__)
app.config.from_object('configs')
app.register_blueprint(rum)

@app.route('/fuckyou')
def fuckyou(title='fuck'):
    return 'Fuck you Cunt'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)