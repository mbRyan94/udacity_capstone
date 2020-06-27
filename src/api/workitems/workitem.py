from flask import abort, request
from flask_restful import Resource
import sys
import os
import requests

from src.authentication.auth import require_auth, AuthError

from src.db.models import Workitem
import src.db.query as db


class Workitem(Resource):
    @require_auth('get:workitem')
    def get(self, jwt_payload, workitem_id):
        try:

            print('workitem: ', workitem_id)
            workitem = db.get_workitem_by_id(workitem_id)
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
                'duration': workitem.duration
            }
        except Exception:
            print(sys.exc_info())
            abort(500)

    @require_auth('delete:workitem')
    def delete(self, jwt_payload, workitem_id):
        try:
            print('workitem_id: ', workitem_id)
            workitem = db.get_workitem_by_id(workitem_id)
            print(workitem)
            test = workitem.delete()
            if not test:
                print(sys.exc_info())
            print('test: ', test)
            return {'msg': 'works'}

        except Exception:
            print(sys.exc_info())
            abort(500)

    # @require_auth('post:workitem')
    # def post(self, jwt_payload):
    #     try:
    #         res_data = []
    #         req_data = request.get_json()
    #         print('req_data: ', req_data)

    #         name = req_data['name']
    #         description = req_data['description']
    #         duration = req_data['duration']
    #         workspace_id = req_data['workspace_id']

    #         new_workitem = Workitem(
    #             name=name, description=description, duration=duration, workspace_id=workspace_id)

    #         if not (new_workitem):
    #             print(sys.exc_info())
    #             return {
    #                 'success': False,
    #                 'error': 400,
    #                 'message': 'bad request'
    #             }
    #         workitem = Workitem.insert(new_workitem)
    #         print('workitem: ', workitem)
    #         return {'msg': 'works'}
    #         # return {
    #         #     'id': workitem.id,
    #         #     'name': workitem.name,
    #         #     'description': workitem.description,
    #         #     'duration': workitem.duration
    #         # }
    #     except Exception:
    #         print(sys.exc_info())
    #         abort(500)
