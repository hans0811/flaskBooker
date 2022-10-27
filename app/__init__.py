from flask import Flask
from flask_login import LoginManager
from app.models.book import db

login_manager = LoginManager()


# @login_manager.user_loader
# def load_usr(user_id):
#     from app.models.user import User
#     user = db.session.query(User).get(user_id)
#     return user


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = 'Please login'
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
