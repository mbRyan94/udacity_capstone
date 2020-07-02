from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Workspace as db_Workspace
from src.authentication.auth import require_auth, AuthError, get_token_user_id
import src.db.query as db

# /projects/:id/workspaces


class Workspaces(Resource):
    method_decorators = [require_auth('get:workspaces')]

    def get(self, jwt_payload, project_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            print('user_id: ', user_id)
            is_users_project = db.check_project_ownership(user_id, project_id)
            if not is_users_project:
                raise AuthError({
                    'status': 'invalid_project_permission',
                    'description': 'action is not allowed for this user'
                }, 401)
            workspaces = db.get_all_workspaces_by_project_and_user(
                user_id, project_id)
            res = []
            for workspace in workspaces:

                res.append({
                    "name": workspace.name,
                    "description": workspace.description,
                    "price": workspace.price,
                    "project_id": workspace.project_id
                })
            return jsonify({
                "success": True,
                "workspaces": res
            })
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)

    method_decorators = [require_auth('post:workspaces')]

    def post(self, jwt_payload, project_id):
        try:

            user_id = get_token_user_id(jwt_payload)
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            price = req_data['price']

            print('project_id: ', project_id)
            is_users_project = db.check_project_ownership(user_id, project_id)
            if not is_users_project:
                raise AuthError({
                    'status': 'invalid_project_permission',
                    'description': 'action is not allowed for this user'
                }, 401)
            new_workspace = db_Workspace(
                name=name, description=description, price=price, project_id=project_id)
            db_Workspace.insert(new_workspace)

            workspaces = db.get_all_workspaces_by_project_and_user(
                user_id, project_id)

            if not workspaces:
                print(sys.exc_info())
                abort(404)
            res = []
            for workspace in workspaces:

                res.append({
                    "name": workspace.name,
                    "description": workspace.description,
                    "price": workspace.price,
                    "project_id": workspace.project_id
                })
            return jsonify({
                "success": True,
                "workspaces": res
            })
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)
