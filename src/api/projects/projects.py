from flask import request, abort, jsonify
from flask_restful import Resource
import sys
import datetime
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Project
from src.authentication.auth import require_auth, AuthError


class Projects(Resource):
    @require_auth('get:projects')
    def get(self, jwt_payload):
        projects = []
        try:
            projects_from_db = Project.query.all()
        except SQLAlchemyError:
            print(sys.exc_info())
            abort(404)

        for project in projects_from_db:
            projects.append({
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'start_date': project.start_date,
                'end_date': project.end_date,

            })
        return jsonify(projects)

    @require_auth('post:projects')
    def post(self, jwt_payload):
        try:
            req_data = request.get_json()
            print(req_data)
            name = req_data['name']
            description = req_data['description']
            start_date = datetime.datetime.now()
            end_date = start_date

            new_project = Project(
                name=name, description=description, start_date=start_date, end_date=end_date)
            Project.insert(new_project)
            projects = Project.query.all()
            res = []
            for project in projects:

                res.append({
                    "name": project.name,
                    "description": project.description,
                    "start_date": project.start_date,
                    "end_date": project.end_date
                })
            # print(res)
            return jsonify({"new_project": res})
        except Exception:
            print(sys.exc_info())
            return jsonify({"new_person": "did not work"})
