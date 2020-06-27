from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Workspace as db_Workspace
from src.authentication.auth import require_auth, AuthError
import src.db.query as db

# /projects/:id/workspaces


class Workspaces(Resource):
    @require_auth('get:workspaces')
    def get(self, jwt_payload):
        try:
            req_data = request.get_json()
            print(req_data)
            return {'msg': 'works'}
        except Exception:
            print(sys.exc_info())
            abort(500)
