from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
import werkzeug
from sqlalchemy.exc import SQLAlchemyError

import src.db.query as db
from src.db.models import Project as db_Project
from src.authentication.auth import require_auth, AuthError, get_token_user_id


class Project(Resource):
    method_decorators = [require_auth('get:project')]

    def get(self, jwt_payload, project_id):
        try:
            user_id = get_token_user_id(jwt_payload)

            project = db.get_project_by_id_and_user(
                user_id, project_id)
            if not project:
                print(sys.exc_info())
                abort(404)

            project_workspaces = []
            workspaces = db.get_all_workspaces_by_project_and_user(
                user_id, project_id)

            if not workspaces:
                print(sys.exc_info())
                abort(404)

            for workspace in workspaces:
                project_workspaces.append({
                    "name": workspace.name,
                    "description": workspace.description,
                    "price": workspace.price,
                    "project_id": workspace.project_id
                })

            return jsonify({
                'success': True,
                'project': project.format(),
                'workspaces': project_workspaces
            })
        except werkzeug.exceptions.NotFound:
            print(sys.exc_info())
            abort(404)
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)

    method_decorators = [require_auth('delete:project')]

    def delete(self, jwt_payload, project_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            project = db.get_project_by_id_and_user(
                user_id, project_id)
            if not project:
                print(sys.exc_info())
                abort(404)
            delete = project.delete()

            if not delete:
                print(sys.exc_info())
            updated_projects = db.get_all_projects_by_user_id(user_id)

            res_data = []
            for project in updated_projects:
                res_data.append({
                    'id': project.id,
                    'name': project.name,
                    'description': project.description,
                    'user_id': project.user_id,
                    'start_date': project.start_date,
                    'end_date': project.end_date
                })
            return jsonify({
                'success': True,
                'projects': res_data
            })
        except werkzeug.exceptions.NotFound:
            print(sys.exc_info())
            abort(404)
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)
