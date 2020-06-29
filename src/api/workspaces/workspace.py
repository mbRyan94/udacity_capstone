from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Workspace as db_Workspace
from src.authentication.auth import require_auth, AuthError, get_token_user_id
import src.db.query as db


class Workspace(Resource):
    method_decorators = [require_auth('get:workspace')]

    def get(self, jwt_payload, project_id, workspace_id):
        try:
            # print('proj_id: ', project_id)
            # print('workspace_id: ', workspace_id)
            user_id = get_token_user_id(jwt_payload)

            workspace = db.get_workspace_by_id_project_id_and_user_id(
                user_id, project_id, workspace_id)
            print('ws: ', workspace)
            if not workspace:
                print(sys.exc_info())
                return {
                    'success': False,
                    'error': 404,
                    'message': 'resource not found'
                }

            workitems = db.get_all_workitems_by_workspace_id(workspace_id)

            res_workitems = []
            for workitem in workitems:
                res_workitems.append({
                    'id': workitem.id,
                    'name': workitem.name,
                    'description': workitem.description,
                    'duration': workitem.duration,
                })

            return {
                'success': True,
                'workspace': workspace.format(),
                'workitems': res_workitems
            }

        except Exception:
            print(sys.exc_info())
            return {
                'success': False,
                'error': 500,
                'message': 'SERVER ERROR'
            }
