from flask import Flask, Blueprint

app = Flask(__name__)


www = Blueprint('www', 'www', url_prefix='/rum')
@www.route('/')
def www_index():
    return 'www'


api = Blueprint('api', 'api', url_prefix='/')
@api.route('/')
def api_index():
    return 'api'


@www.route('/why')
def why_page():
    return 'Why not rum?'



if __name__ == '__main__':
    app.register_blueprint(api)
    app.register_blueprint(www)
    app.run(host='localhost', port=5000, debug=True)
