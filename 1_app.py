__author__ = 'spousty'

from bottle import route, run, DEBUG
import os


@route('/')
def index():
    return "<h1> Vagrant and VirtualBox is fun</h1>"


"Hello proper Person"
    run(host='0.0.0.0', port=8080, debug=True)
