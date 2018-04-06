import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import \
    declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

ECHO = False

ENGINE = create_engine('sqlite:///:memory:',
                       echo=ECHO)

Session = sessionmaker(bind=ENGINE)
SESSION = Session()


class DBObject(object):
    def delete(self):
        pass

    def __repr__(self):
        return "<DB:{}(id={}, name={})>".format(
            self.__class__.__name__,
            self.id, self.name)


class User(Base, DBObject):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    passwdHash = Column(String)
    email = Column(String)
    tel = Column(String)
    date = Column(DateTime)
    comp = Column(String)

    def __init__(self,
                 name,
                 email,
                 tel,
                 comp,
                 date=None,
                 id=None):

        if id is not None:
            self.id = id
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
        self.tel = tel
        self.comp = comp
        self.email = email
        self.name = name
        self.passwdHash = ""

    def setpasswd(self, passwd):
        self.passwdHash = hash(passwd)
        return self.passwdHash


class Recipe(Base, DBObject):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    totalTime = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User,
                        back_populates="recipes")

    def __init__(self, user, name, id=None):
        self.name = name
        if id is not None:
            self.id = id
        self.user = user


User.recipes = relationship(
    Recipe,
    order_by=User.id,
    back_populates="user")


def init():
    Base.metadata.create_all(ENGINE)
