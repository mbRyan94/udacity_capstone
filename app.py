import os
from flask import Flask, jsonify, request, abort
import datetime
from flask_heroku import Heroku
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
import sys
from urllib.error import HTTPError

from src.db.models import setup_db, Project, Workspace, Workitem
from src.authentication.auth import require_auth, AuthError
from src.api.routes import initialize_routes

load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    api = Api(app)
    heroku = Heroku(app)
    setup_db(app)
    app.config["SQLALCHEMY_DATABASE_URI"]
    initialize_routes(api)

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
    @require_auth('get:workspaces')
    def api_test(jwt_payload):
        try:
            return jsonify({"msg": jwt_payload})

        except Exception:
            print(sys.exc_info())
            abort(404)

    # @app.route('/api/projects', methods=['POST'])
    # @require_auth('post:projects')
    # def add_project(jwt_payload):
    #     try:
    #         req_data = request.get_json()
    #         print(req_data)
    #         name = req_data['name']
    #         description = req_data['description']
    #         start_date = datetime.datetime.now()
    #         end_date = start_date
    #         print('end_time: ', end_date)
    #         print(req_data)
    #         new_project = Project(
    #             name=name, description=description, start_date=start_date, end_date=end_date)
    #         Project.insert(new_project)
    #         projects = Project.query.all()
    #         res = []
    #         for project in projects:

    #             res.append({
    #                 "name": project.name,
    #                 "description": project.description,
    #                 "start_date": project.start_date,
    #                 "end_date": project.end_date
    #             })
    #         # print(res)
    #         return jsonify({"new_project": res})
    #     except Exception:
    #         print(sys.exc_info())
    #         return jsonify({"new_person": "did not work"})

    # @app.route('/api/projects')
    # @require_auth('get:projects')
    # def get_all_projects(jwt_payload):
    #     try:
    #         projects_from_db = Project.query.all()
    #         print('projects', projects_from_db)
    #     except Exception:
    #         print(sys.exc_info())
    #         return jsonify({
    #             'success': False
    #         })
    #         projects = []
    #         for project in projects_from_db:
    #             projects.append(
    #                 {
    #                     id: project.id,
    #                     name: project.name,
    #                     description: project.description,
    #                     start_date: project.start_date,
    #                     end_date: project.end_date,
    #                     workspaces: [project.workspaces]
    #                 }
    #             )
    #         return jsonify({
    #             'success': True,
    #             'projects': projects
    #         })

    # @app.route('/api/workspaces', methods=['POST'])
    # def add_workspaces():
    #     try:
    #         req_data = request.get_json()
    #         print(req_data)
    #         name = req_data['name']
    #         description = req_data['description']
    #         price = req_data['price']
    #         project_id = req_data['project_id']
    #         print('project_id: ', project_id)
    #         print(req_data)
    #         new_workspace = Workspace(
    #             name=name, description=description, price=price, project_id=project_id)
    #         Workspace.insert(new_workspace)
    #         workspaces = Workspace.query.all()
    #         res = []
    #         for workspace in workspaces:

    #             res.append({
    #                 "name": workspace.name,
    #                 "description": workspace.description,
    #                 "price": workspace.price,
    #                 "project_id": workspace.project_id
    #             })
    #         # print(res)
    #         return jsonify({"new_workspace": res})
    #     except Exception:
    #         print(sys.exc_info())
    #         return jsonify({"new_workspace": "did not work"})

    @app.route('/api/workitems', methods=['POST'])
    def add_workitem():
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

    # @app.route('/api/users', methods=['POST'])
    # def add_user():
    #     try:
    #         req_data = request.get_json()
    #         print(req_data)
    #         name = req_data['name']
    #         email = req_data['email']

    #         new_user = User(
    #             name=name, email=email)
    #         User.insert(new_user)
    #         users = User.query.all()
    #         res_names = []
    #         for user in users:

    #             res_names.append({
    #                 "name": user.name,
    #                 "email": user.email
    #             })
    #         # print(res)
    #         return jsonify({"new_user": res_names})
    #     except Exception:
    #         print(sys.exc_info())
    #         return jsonify({"new_user": "did not work"})

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 400

    @app.errorhandler(401)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }), 401

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'SERVER ERROR'
        }), 500

    @app.errorhandler(AuthError)
    def authentication_error(error):
        print(error)
        error_status_code = error.status_code
        error_description = error.error['description']
        return jsonify({
            'success': False,
            'error': error_status_code,
            'message': error_description
        })

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
