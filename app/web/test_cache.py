from flask import make_response, session

from . import web


@web.route('/set/cookie')
def set_cookie():
    response = make_response('Hello MR.7')
    response.set_cookie('name', 'MR.7', 100)
    return response


@web.route('/set/session')
def set_session():
    session['t'] = 1
    return 'over'

@web.route('/get/session')
def get_session():
    return str(session['t'])