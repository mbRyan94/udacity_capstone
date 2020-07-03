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
import src.error_handlers.error_handlers as errors

load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    api = Api(app, errors=errors)
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
                name=name, description=description,
                duration=duration, workspace_id=workspace_id)
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

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }), 401

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(500)
    def server_error(error):
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
