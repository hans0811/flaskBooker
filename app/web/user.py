from flask import Blueprint

from app.web import web


#  user = Blueprint('user', __name__)

@web.route('/url')
def login():
    pass