from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Project as db_Project
from src.authentication.auth import require_auth, AuthError


class Project(Resource):
    # @require_auth('get:project')
    def get(self, project_id):
        try:
            project = db_Project.query.filter(
                db_Project.id == project_id).first()
            print(project.format())
            return jsonify({
                'success': True,
                'project': project.format()
            })

        except Exception:
            print(sys.exc_info())
            abort(404)
