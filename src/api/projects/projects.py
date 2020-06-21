from flask import request, abort, jsonify
from flask_restful import Resource
import sys
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Project


class Projects(Resource):
    def get(self):
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
