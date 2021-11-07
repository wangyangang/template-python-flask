from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort


bp = Blueprint("port_scanner", __name__)


@bp.route("/")
def index():
    return "abc"


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 443

def scan(port):
    if s.connect_ex((host, port)):
        print('the port is closed.')
    else:
        print('the port is open.')

# scan(443)


