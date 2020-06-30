from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.authentication.auth import require_auth, AuthError, get_token_user_id

from src.db.models import Workitem as db_Workitem
import src.db.query as db


class Workitem(Resource):
    method_decorators = [require_auth('get:workitem')]

    def get(self, jwt_payload, project_id, workspace_id, workitem_id):
        try:
            user_id = get_token_user_id(jwt_payload)
            print('work: ', db.get_workitem_by_id_project_id_user_id_and_workspace_id(
                user_id, project_id, workspace_id, workitem_id))
            print('workitem: ', workitem_id)
            workitem = db.get_workitem_by_id_project_id_user_id_and_workspace_id(
                user_id, project_id, workspace_id, workitem_id)
            if not workitem:
                print(sys.exc_info())
                return {
                    'success': False,
                    'error': 404,
                    'message': 'resource not found'
                }
            return {
                'id': workitem.id,
                'name': workitem.name,
                'description': workitem.description,
                'duration': workitem.duration,
                'workspace_id': workitem.workspace_id
            }
        except Exception:
            print(sys.exc_info())
            abort(500)

    method_decorators = [require_auth('patch:workitem')]

    def patch(self, jwt_payload, project_id, workspace_id, workitem_id):
        try:
            req_data = request.get_json()
            print('req_data: ', req_data)
            # name = req_data['name']
            # description = req_data['description']
            # duration = req_data['duration']

            user_id = get_token_user_id(jwt_payload)
            print('work: ', db.get_workitem_by_id_project_id_user_id_and_workspace_id(
                user_id, project_id, workspace_id, workitem_id))

            workitem = db.get_workitem_by_id_project_id_user_id_and_workspace_id(
                user_id, project_id, workspace_id, workitem_id)
            if not workitem:
                print(sys.exc_info())
                return {
                    'success': False,
                    'error': 404,
                    'message': 'resource not found'
                }
            if 'name' in req_data:
                workitem.name = req_data['name']
            if 'description' in req_data:
                workitem.description = req_data['description']
            if 'duration' in req_data:
                workitem.duration = req_data['duration']

            workitem.update()
            updated_workitem = db.get_workitem_by_id_project_id_user_id_and_workspace_id(
                user_id, project_id, workspace_id, workitem_id)

            return {'workitem': updated_workitem.format()}

        except Exception:
            print(sys.exc_info())
            abort(500)
