from flask import request, abort, jsonify
from flask_restful import Resource
import sys
import json
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Project
from src.authentication.auth import require_auth, AuthError, get_token_user_id
import src.db.query as db


class Projects(Resource):
    method_decorators = [require_auth('get:projects')]

    def get(self, jwt_payload):
        projects = []
        try:
            jwt_subject = jwt_payload['sub']

            user_id = jwt_subject.split('|')[1]

            projects_from_db = db.get_all_projects_by_user_id(user_id)
        except SQLAlchemyError:
            print(sys.exc_info())
            abort(404)
        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)

        for project in projects_from_db:
            projects.append({
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'start_date': project.start_date,
                'end_date': project.end_date,
                'user_id': project.user_id

            })
        return jsonify({
            'success': True,
            'projects': projects
        })

    method_decorators = [require_auth('post:projects')]

    def post(self, jwt_payload):
        try:
            req_data = request.get_json()

            if not req_data:
                print(sys.exc_info())
                abort(400)
            name = req_data['name']
            description = req_data['description']
            start_date = datetime.now().date()

            end_date = start_date + timedelta(days=14)
            user_id = get_token_user_id(jwt_payload)

            new_project = Project(
                name=name, description=description, start_date=start_date,
                end_date=end_date, user_id=user_id)
            Project.insert(new_project)
            projects = db.get_all_projects_by_user_id(user_id)
            if not projects:
                print(sys.exc_info())
                abort(404)
            res = []
            for project in projects:

                res.append({
                    "name": project.name,
                    "description": project.description,
                    "start_date": json.dumps(project.start_date, indent=4,
                                             sort_keys=True, default=str),
                    "end_date": json.dumps(project.end_date, indent=4,
                                           sort_keys=True, default=str),
                    "user_id": project.user_id
                })

            return {
                "success": True,
                "projects": res
            }

        except AuthError:
            print(sys.exc_info())
            abort(401)
        except Exception:
            print(sys.exc_info())
            abort(500)
