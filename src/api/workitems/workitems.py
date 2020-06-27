from flask import abort, request
from flask_restful import Resource
import sys
import os
import requests

from src.authentication.auth import require_auth, AuthError, get_token_auth_header

from src.db.models import Workitem
import src.db.query as db


class Workitems(Resource):
    @require_auth('post:workitems')
    def post(self, jwt_payload):
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
            if not new_item:
                abort(400)
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

            return {"new_workspace": res}
        except Exception:
            print(sys.exc_info())
            return {
                "success": False,
                "error": 500,
                "message": "SERVER ERROR"
            }

    @require_auth('get:workitems')
    def get(self, jwt_payload):
        try:
            workspace_id = request.args.get('workspace_id')
            print('workspace_id: ', workspace_id)
            workitems = db.get_workitems_by_workspace_id(workspace_id)
            if not workitems:
                print(sys.exc_info())
                abort(404)

            res_data = []
            for item in workitems:
                res_data.append({
                    'id': item.id,
                    'name': item.name,
                    'description': item.description,
                    'duration': item.duration
                })
            return {
                'success': True,
                'workitems': res_data
            }
        except Exception:
            print(sys.exc_info())
            abort(500)

# client:
#     /projects/: id
#     /workspaces/: id
#     /workitems/: id

# backend:
#     /api/user_id/projects/project_id/workspaces/id/Workitems/id

#     /api/projects?user_id = xxx
#     /api/workspaces?user_id = xxx
#     /api/Workitems?user_id = xxx

#     Select *
#     from worspace
#     where project_id = (
#         Select id
#         from project
#         where project.user_id=user_id
#     )
