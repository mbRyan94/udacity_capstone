from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Workitem as db_Workitem
from src.authentication.auth import require_auth, AuthError, get_token_user_id
import src.db.query as db


class Workitems(Resource):
    method_decorators = [require_auth('post:workitems')]

    def post(self, jwt_payload, project_id, workspace_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            is_users_project = db.check_project_and_workspace_ownership(
                user_id, project_id, workspace_id)
            if not is_users_project:
                raise AuthError({
                    'status': 'invalid_project_and_workspace_permission',
                    'description': 'action is not allowed for this user'
                }, 401)
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            duration = req_data['duration']

            print('workspace_id: ', workspace_id)

            new_item = db_Workitem(
                name=name, description=description, duration=duration, workspace_id=workspace_id)

            db_Workitem.insert(new_item)
            workitems = db.get_all_workitems_by_workspace_id(
                workspace_id)
            if not workitems:
                print(sys.exc_info())
                abort(404)
            res_data = []
            for workitem in workitems:

                res_data.append({
                    "name": workitem.name,
                    "description": workitem.description,
                    "duration": workitem.duration,
                    "workspace_id": workitem.workspace_id
                })

            return {
                "success": True,
                "workitems": res_data
            }
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)

    method_decorators = [require_auth('get:workitems')]

    def get(self, jwt_payload, project_id, workspace_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            is_users_project = db.check_project_and_workspace_ownership(
                user_id, project_id, workspace_id)
            if not is_users_project:
                raise AuthError({
                    'status': 'invalid_project_and_workspace_permission',
                    'description': 'action is not allowed for this user'
                }, 401)

            workitems = db.get_all_workitems_by_workspace_id(
                workspace_id)
            res_data = []
            for workitem in workitems:

                res_data.append({
                    "name": workitem.name,
                    "description": workitem.description,
                    "duration": workitem.duration,
                    "workspace_id": workitem.workspace_id
                })

            return {
                "success": True,
                "workitems": res_data
            }

        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)
