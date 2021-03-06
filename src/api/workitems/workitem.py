from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
import werkzeug
from sqlalchemy.exc import SQLAlchemyError


from src.authentication.auth import require_auth, AuthError, get_token_user_id

from src.db.models import Workitem as db_Workitem
import src.db.query as db


class Workitem(Resource):
    method_decorators = [require_auth('get:workitem')]

    def get(self, jwt_payload, project_id, workspace_id, workitem_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            workitem = db.get_users_workitem(
                user_id, project_id, workspace_id, workitem_id)
            if not workitem:
                print(sys.exc_info())
                abort(404)
            return {
                'success': True,
                'workitem': {
                    'id': workitem.id,
                    'name': workitem.name,
                    'description': workitem.description,
                    'duration': workitem.duration,
                    'workspace_id': workitem.workspace_id
                }

            }
        except werkzeug.exceptions.NotFound:
            print(sys.exc_info())
            abort(404)
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)

    method_decorators = [require_auth('patch:workitem')]

    def patch(self, jwt_payload, project_id, workspace_id, workitem_id):
        try:
            req_data = request.get_json()
            user_id = get_token_user_id(jwt_payload)

            workitem = db.get_users_workitem(
                user_id, project_id, workspace_id, workitem_id)
            if not workitem:
                print(sys.exc_info())
                abort(404)
            if 'name' in req_data:
                workitem.name = req_data['name']
            if 'description' in req_data:
                workitem.description = req_data['description']
            if 'duration' in req_data:
                workitem.duration = req_data['duration']

            workitem.update()
            updated_workitem = db.get_users_workitem(
                user_id, project_id, workspace_id, workitem_id)

            return {
                'success': True,
                'workitem': updated_workitem.format()
            }

        except werkzeug.exceptions.NotFound:
            print(sys.exc_info())
            abort(404)
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)
