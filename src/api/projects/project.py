from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Project as db_Project
from src.authentication.auth import require_auth, AuthError


class Project(Resource):
    decorators = [require_auth('get:project')]

    def get(self, jwt_payload, project_id):
        try:
            print('jwt: ', jwt_payload)
            project = db_Project.query.filter(
                db_Project.id == project_id).first()
            if not project:
                return {
                    'success': False,
                    'error': 404,
                    'message': 'resource not found'
                }

            print(project.format())
            return jsonify({
                'success': True,
                'project': project.format()
            })

        except Exception:
            print(sys.exc_info())
            abort(500)
