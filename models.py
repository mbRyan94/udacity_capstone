import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import app
from dotenv import load_dotenv
load_dotenv()

# print(os.getenv('DATABASE_URL'))
# database_path = os.getenv('DATABASE_URL')

# HEROKU POSTGRES SETUP
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    # db.drop_all()
    db.create_all()


'''
Person
Have title and release year
'''


class Person(db.Model):
    __tablename__ = 'People'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    catchphrase = Column(db.String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase}

    def insert(self):
        db.session.add(self)
        db.session.commit()


class Dog(db.Model):
    __tablename__ = 'Dog'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    catchphrase = Column(db.String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def insert(self):
        db.session.add(self)
        db.session.commit()
