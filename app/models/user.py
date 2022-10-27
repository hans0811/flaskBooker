"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float

__author__ = '七月'

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.booker_book import BookerBook


class User(UserMixin, Base):
    # __tablename__ = 'user1'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        booker_book = BookerBook()
        booker_book.search_by_isbn(isbn)
        if not booker_book.first:
            return False
        # Not allow user can donate the same book at the same time
        # Can not allow user be a asker or donor
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        gifting = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()

        if not gifting and not wishing:
            re


    # if not using UserMixin, we need to create function
    # def get_id(self):
    #     return self.id

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))