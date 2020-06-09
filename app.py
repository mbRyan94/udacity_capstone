import os
from flask import Flask, jsonify, request
import datetime
from flask_heroku import Heroku
from models import setup_db, Project, Workspace, Workitem, User
from flask_cors import CORS
from dotenv import load_dotenv
import sys
load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)

    heroku = Heroku(app)
    setup_db(app)
    app.config["SQLALCHEMY_DATABASE_URI"]

    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.getenv('EXCITED')
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/api/test')
    def api_test():
        return jsonify({"msg": "API is working!"})

    @app.route('/api/projects', methods=['POST'])
    def db_add_person():
        try:
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            start_date = datetime.datetime.now()
            end_date = start_date
            print('end_time: ', end_date)
            print(req_data)
            new_project = Project(
                name=name, description=description, start_date=start_date, end_date=end_date)
            Project.insert(new_project)
            projects = Project.query.all()
            res = []
            for project in projects:
                # print('person: ', person)
                res.append({
                    "name": project.name,
                    "description": project.description
                })
            # print(res)
            return jsonify({"new_project": res})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_person": "did not work"})

    @app.route('/api/workspaces', methods=['POST'])
    def db_add_workspaces():
        try:
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            price = req_data['price']
            project_id = req_data['project_id']
            print('project_id: ', project_id)
            print(req_data)
            new_workspace = Workspace(
                name=name, description=description, price=price, project_id=project_id)
            Workspace.insert(new_workspace)
            workspaces = Workspace.query.all()
            res = []
            for workspace in workspaces:
                # print('person: ', person)
                res.append({
                    "name": workspace.name,
                    "description": workspace.description,
                    "price": workspace.price,
                    "project_id": workspace.project_id
                })
            # print(res)
            return jsonify({"new_workspace": res})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_workspace": "did not work"})

    @app.route('/api/workitems', methods=['POST'])
    def db_add_workitem():
        try:
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            duration = req_data['duration']
            workspace_id = req_data['workspace_id']
            print('workspace_id: ', workspace_id)
            print(req_data)
            new_item = Workitem(
                name=name, description=description, duration=duration, workspace_id=workspace_id)
            Workitem.insert(new_item)
            workitems = Workitem.query.all()
            res = []
            for workitem in workitems:
                # print('person: ', person)
                res.append({
                    "name": workitem.name,
                    "description": workitem.description,
                    "duration": workitem.duration,
                    "project_id": workitem.workspace_id
                })
            # print(res)
            return jsonify({"new_workspace": res})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_workspace": "did not work"})

    @app.route('/api/users', methods=['POST'])
    def add_user():
        try:
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            email = req_data['email']

            new_user = User(
                name=name, email=email)
            User.insert(new_user)
            users = User.query.all()
            res_names = []
            for user in users:
                # print('person: ', person)
                res_names.append({
                    "name": user.name,
                    "email": user.email
                })
            # print(res)
            return jsonify({"new_user": res_names})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_user": "did not work"})

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
