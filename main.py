
from flask import Flask, request, render_template
from functools import wraps
import datetime
from device import Device
from typing import List, Dict

app = Flask(__name__)

checkins = 0

known_clients: Dict[str, Device] = {}


def check_auth(*args) -> bool:
    return True


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if not (auth and check_auth(auth.username, auth.password)):
            return ('Unauthorized', 401, {
                'WWW-Authenticate': 'Basic realm="Login Required"'
            })

        return f(**kwargs)

    return wrapped_view


@app.route("/")
def hello_world():
    return "<p>Hello this is WatchGoat!</p><br><img src=\"https://i.imgur.com/yBxMPT3.png\" alt=\"Retarded Goat\">"


@app.route("/get_list")
def get_list():
    global known_clients
    return render_template("list.html", known_clients=known_clients)


@app.route("/goat", methods=['GET', 'POST'])
@login_required
def goat():
    global checkins
    global known_clients
    checkins = checkins + 1
    print(request.headers)
    print(f"Username : {request.authorization.username} -- data : {request.get_json()}")

    username = request.authorization.username
    ip = request.get_json()

    dev = Device(ip)

    known_clients[username] = dev

    return f"testing goat; Hello {request.authorization.username}; Check-ins : {checkins}"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
