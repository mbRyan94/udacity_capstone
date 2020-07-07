import unittest
import os
import json
import sys

from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from dotenv import load_dotenv
from importlib.machinery import SourceFileLoader
from app import create_app
import src.db.models as db
import src.db.query as query

load_dotenv()

# A token from a user with the freelancer role assigned
token = os.environ['freelancer_token']

# A token WITHOUT openID scopes to fetch Auth0 /userinfo endpoint
restricted_permission_token = os.environ['intern_token_no_openId_scope']

# token from intern role without project delete and post permission
intern_token = os.environ['intern_token']


class TestCases(unittest.TestCase):
    def setUp(self):
        try:
            self.app = create_app()
            self.client = self.app.test_client

            self.database_name = "test_db"
            self.database_path = "postgresql://{}/{}".format(
                'localhost:5432', self.database_name)
            db.setup_db(self.app, self.database_path)

            with self.app.app_context():
                self.db = SQLAlchemy()
                self.db.init_app(self.app)
                self.db.create_all()
        except Exception:
            print(sys.exc_info())

        self.new_project = {
            "name": "TestProject ",
            "description": "Test Client - Biz and Marketing",
            "user_id": "5ee344e01fb8c3001471413c"
        }

        self.new_workspace = {
            "name": "Marketing",
            "description": "Marketing stuff",
            "price": 100
        }

        self.new_workitem = {
            "name": "Social Media Campaign",
            "description": "creating leads campaign",
            "duration": 20
        }

        self.patch_workitem = {
            "name": "SEO Campaign",
            "description": "optimize website to make google"
            "fall in love with it <3",
            "duration": 7
        }

    # test projects routes

    def test_get_projects_by_user_id(self):
        res = self.client().get(
            '/api/projects',
            headers={'Authorization': 'Bearer {}'.format(token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['projects'])

    def test_get_projects_by_user_id_without_authorization_headers(self):
        res = self.client().get('/api/projects')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_post_new_project_success(self):
        res = self.client().post('/api/projects',
                                 json=self.new_project,
                                 headers={
                                     'Authorization': 'Bearer {}'.format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['projects']) != 0)
        self.assertTrue(data['success'])

    def test_post_new_project_failure(self):
        res = self.client().post('/api/projects/1', json=self.new_project,
                                 headers={
                                     'Authorization': 'Bearer {}'.format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])

    # test project routes
    def test_get_project_success(self):
        res = self.client().get('api/projects/29',
                                headers={
                                    'Authorization': 'Bearer {}'.format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['project'])
        self.assertTrue(data['project']['id'])

    def test_get_project_failure(self):
        res = self.client().get('api/projects/-1',
                                headers={
                                    'Authorization': 'Bearer {}'.format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_delete_project_success(self):
        res = self.client().delete('/api/projects/27',
                                   headers={
                                       'Authorization':
                                       'Bearer {}'.format(token)
                                   })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    # try to delete another users project
    def test_delete_project_wrong_user_failure(self):
        res = self.client().delete('/api/projects/22',
                                   headers={
                                       'Authorization': 'Bearer {}'
                                       .format(intern_token)
                                   })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    # using the intern token which does not have the post:project permission
    def test_post_project_missing_permission_failure(self):
        res = self.client().post('/api/projects',
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(intern_token)
                                 },
                                 json=self.new_project)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    # using the intern token which does not have the delete:project permission
    def test_delete_project_wrong_user_failure(self):
        res = self.client().delete('/api/projects/32',
                                   headers={
                                       'Authorization': 'Bearer {}'
                                       .format(intern_token)
                                   })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    # test workspace routes

    def test_get_user_and_project_specific_workspaces_success(self):
        res = self.client().get('/api/projects/29/workspaces',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['workspaces'])

    def test_get_user_and_project_specific_workspaces_failure(self):
        # user has no permission to access project 31s workspaces.
        # it is relatated to another user
        res = self.client().get('/api/projects/31/workspaces',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_post_new_workspace_success(self):
        res = self.client().post('/api/projects/29/workspaces',
                                 json=self.new_workspace,
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['workspaces'])
        self.assertTrue(data['success'])

    def test_post_new_workspace_failure(self):
        res = self.client().post('/api/projects/31/workspaces',
                                 json=self.new_workspace,
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    # test workpace routes
    def test_get_workspace_success(self):
        res = self.client().get('api/projects/29/workspaces/39',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['workspace'])
        self.assertEqual(data['workspace']['id'], 39)

    def test_get_workspace_failure(self):
        res = self.client().get('api/projects/29/workspaces/41',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # workitems routes
    def test_get_user_and_project_specific_workitems_success(self):
        res = self.client().get('/api/projects/29/workspaces/35/workitems',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['workitems'])

    def test_get_user_and_project_specific_workitems_failure(self):
        # user has no permission to access project 31s workspaces.
        # They are relatated to diff user
        res = self.client().get('/api/projects/31/workspaces/41/workitems',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_post_new_workitem_success(self):
        res = self.client().post('/api/projects/29/workspaces/39/workitems',
                                 json=self.new_workitem,
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['workitems'])
        self.assertTrue(data['success'])

    def test_post_new_workitem_failure_unauthorized(self):
        res = self.client().post('/api/projects/31/workspaces/41/workitems',
                                 json=self.new_workitem,
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(token)
                                 })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_post_new_workitem_failure_method_not_allowed(self):
        res = self.client().post('/api/projects/31/workspaces/41/workitems/23',
                                 json=self.new_workitem,
                                 headers={
                                     'Authorization': 'Bearer {}'
                                     .format(token)
                                 })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])

    # test workitem routes
    def test_patching_workitem_success(self):
        res = self.client().patch(
            '/api/projects/29/workspaces/35/workitems/17',
            json={
                "name": "task #1",
                "description": "first task to be done"
            },
            headers={
                'Authorization': 'Bearer {}'
                .format(token)
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['workitem']['id'], 17)

    def test_get_workitem_success(self):
        res = self.client().get('api/projects/29/workspaces/35/workitems/17',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['workitem']['name'], 'task #1')
        self.assertEqual(data['workitem']['id'], 17)

    def test_get_workitem_failure(self):
        res = self.client().get('/api/projects/29/workspaces/41/workitems/17',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(token)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_patch_workitem_success(self):
        res = self.client().patch(
            '/api/projects/29/workspaces/35/workitems/17',
            json=self.patch_workitem,
            headers={
                'Authorization': 'Bearer {}'
                .format(token)
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['workitem']['id'], 17)
        self.assertEqual(data['workitem']['duration'], 7.0)

    def test_patch_workitem_name_success(self):
        res = self.client().patch(
            '/api/projects/29/workspaces/35/workitems/17',
            json={"name": "task #1"},
            headers={'Authorization': 'Bearer {}'
                     .format(token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['workitem']['id'], 17)
        self.assertEqual(data['workitem']['duration'], 7.0)

    def test_patch_workitem_failure(self):
        res = self.client().patch(
            '/api/projects/29/workspaces/41/workitems/21',
            json=self.patch_workitem,
            headers={'Authorization': 'Bearer {}'
                     .format(token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # test profile route

    def test_profile(self):
        res = self.client().get(
            '/api/profile', headers={'Authorization': 'Bearer {}'
                                     .format(token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['profile'])

    def test_profile_without_role_permission(self):
        res = self.client().get('/api/profile',
                                headers={
                                    'Authorization': 'Bearer {}'
                                    .format(restricted_permission_token)
                                })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertFalse(data['success'])


if __name__ == "__main__":
    unittest.main()
