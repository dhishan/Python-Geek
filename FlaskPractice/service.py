from functools import wraps
from flask import Flask, request, Response

app = Flask(__name__)


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def root():
    return "Hello"


# curl -i http://127.0.0.1/stats
@app.route('/stats')
def getInfo():
    return "this is from stats"


# curl -i http://127.0.0.1/stats/dhishan/
@app.route('/stats/<string:name>/')
def getInfoMembers(name):
    return "this is from stats name" + str(name)


# curl -u admin:secret http://127.0.0.1/getstats?name=dhishan
# curl -i http://127.0.0.1/getstats?name=dhishan
@app.route('/getstats')
@requires_auth
def getresult():
    return "this is from getReslt" + str(request.args)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
