import os
from sqlalchemy import Column, String, create_engine, DateTime
import datetime
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


class Project(db.Model):
    __tablename__ = 'project'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    description = Column(db.String)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime)
    user_id = Column(db.String, nullable=False)
    workspaces = db.relationship(
        'Workspace', cascade='all, delete-orphan', backref='project')

    def __init__(self, name, description="", start_date=None, end_date=None, user_id=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'user_id': self.user_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Workspace(db.Model):
    __tablename__ = 'workspace'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    description = Column(db.String)
    price = Column(db.Float)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)
    workitems = db.relationship(
        'Workitem', cascade='all, delete-orphan', backref='workspace', lazy=True)

    def __init__(self, name, description="", price=0.0, project_id=None):
        self.name = name
        self.description = description
        self.price = price
        self.project_id = project_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Workitem(db.Model):
    __tablename__ = 'workitem'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    description = Column(db.String)
    duration = Column(db.Float)
    workspace_id = db.Column(db.Integer, db.ForeignKey(
        'workspace.id'), nullable=False)

    def __init__(self, name, description="", duration=0.0, workspace_id=None):
        self.name = name
        self.description = description
        self.duration = duration
        self.workspace_id = workspace_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Test(db.Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
