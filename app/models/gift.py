from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship

from app.models.base import db, Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # User's id is Integer
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
