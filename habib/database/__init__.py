"""The database layer.

In this module we define the (very simple) database layer using SQLAlchemy. In
order to keep things simple for out little exercise, we chose SQLite so that
we wouldn't have to worry about database installation and setup.

The sqlalchemy.ext.declarative.declarative_base method imported below allows us
to create a descriptive base class. This base class can then be used to create
our own table mapping classes. There are lots of interesting things that can be
achieved using the declarative base concept, some of which we will try out in
our project.

Note: SQLAlchemy also allows other ways of interfacing with your database. The
declarative base is just our preferred way of doing things.
"""

from datetime import datetime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Text, Column, DateTime

connection = create_engine("sqlite:///habib.db")

Base = declarative_base()
Session = scoped_session(sessionmaker(bind=connection))


class BlogPost(Base):
    """The SQLAlchemy class for our blog_post table.
    """

    __tablename__ = "blog_post"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(Text, nullable=False)
    post = Column(Text)
    author = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.now())
    modified_date = Column(DateTime, nullable=False, default=datetime.now())
    # TODO:  Enable these once we have users in the system
    # created_by = Column(Integer)
    # modified_by = Column(Integer)


# class Students(Base):
#     __tablename__ = "students"


Base.metadata.create_all(connection)
