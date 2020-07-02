


import unittest
import os
import json
import sys
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
# from models import setup_db, Project, Workspace, Workitem
# from ..app import create_app
from importlib.machinery import SourceFileLoader
from app import create_app
import src.db.models as db
import src.db.query as query

# app = SourceFileLoader("app", "app.py").load_module()
# db = SourceFileLoader("module", "../db/module.py").load_module()
# Please create a new token before running the tests
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWUzNDRlMDFmYjhjMzAwMTQ3MTQxM2MiLCJhdWQiOlsiZnJlZXRpbWUiLCJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTM2NzYxMDcsImV4cCI6MTU5MzY4MzMwNywiYXpwIjoidk96YW9uanJmZmdQZGE3dUhOUTRxR3FySDRJdkV2aFUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6d29ya2l0ZW0iLCJnZXQ6cHJvZmlsZSIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3RzIiwiZ2V0OndvcmtpdGVtIiwiZ2V0OndvcmtpdGVtcyIsImdldDp3b3Jrc3BhY2UiLCJnZXQ6d29ya3NwYWNlcyIsIm9wZW5pZDplbWFpbCIsInBhdGNoOnByb2plY3QiLCJwYXRjaDp3b3JraXRlbSIsInBvc3Q6cHJvamVjdHMiLCJwb3N0OndvcmtpdGVtcyIsInBvc3Q6d29ya3NwYWNlcyJdfQ.EMBjBLTb1YnR7cnlTuAg55A4WJzB13hDI3sju9hEJrGNbL6mqcymN9M1_28NOSqT3yyUIa42MZsrF_vzxrPTkzb4UZfokKPWAv2bVADeH-O6Noowjh1w9UPQINpbeZ1Hsy2-ecqTMsHPS8rULXMlGdXFPK21_EHyS6-rTppki6h3GkC_wDcE_QaDJguh9nFuivSLkwnzIykwpwZx8vLGXxr7zJ84SJlCTaKysSy6saOnU_HYrZ18-FeXot_CwJtZZQiBd8hJoqBHBhTB58OHbVycZerUjnrc6Vs1iG0t7c_H93xtrjr4gPeX9pDUWCxeVMdceDnDcZhXuayZduuIQg'

# A token without openID scopes to fetch Auth0 /userinfo endpoint
restricted_permission_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWUzNDRlMDFmYjhjMzAwMTQ3MTQxM2MiLCJhdWQiOiJmcmVldGltZSIsImlhdCI6MTU5MzY3MDA1MiwiZXhwIjoxNTkzNjc3MjUyLCJhenAiOiJ2T3phb25qcmZmZ1BkYTd1SE5RNHFHcXJINEl2RXZoVSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6d29ya2l0ZW0iLCJnZXQ6cHJvZmlsZSIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3RzIiwiZ2V0OndvcmtpdGVtIiwiZ2V0OndvcmtpdGVtcyIsImdldDp3b3Jrc3BhY2UiLCJnZXQ6d29ya3NwYWNlcyIsIm9wZW5pZDplbWFpbCIsInBhdGNoOnByb2plY3QiLCJwYXRjaDp3b3JraXRlbSIsInBvc3Q6cHJvamVjdHMiLCJwb3N0OndvcmtpdGVtcyIsInBvc3Q6d29ya3NwYWNlcyJdfQ.JI6KJQClODrEb7Tiv-nFdkav_Ln7F9jfSidPc2GCEg3f7Md_atbxaZqhEjUkZG-gDb3ZetkyajJx67prl0dY5pfDskKSPAYWzekk5aokRIECCEvwsZpW7BUNRpPxeDapTzRUAS-rSE-hPccZspfTDLAV8R9M6wJv07PIOn1LtmU3CzQQAAWQzivGou5DPxiIkPdllO_BUYxaU5cB9t8SfJcYoAzofj5LxV-U9HAd_lMYHwmNAM0w7VZn8YAnsXEqStWxugHOS0fnYxar6yLq6GjX7nzh79KRgGgbnF-WGeFWL98eOtv9T0rLnf8qTE8Tr0a1w9_NwZvd-C-ebVFXZw'



class TestCases(unittest.TestCase):
    def setUp(self):
        try:
            self.app = create_app()
            self.client = self.app.test_client
            self.headers = {'Content-Type': 'application/json',
                            'Authorization': 'Bearer {}'.format(token)}
            self.database_name = "test_db"
            self.database_path = "postgresql://{}{}".format(
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

    # test projects routes
    def test_get_projects_by_user_id(self):
        res = self.client().get('/api/projects', headers={'Authorization': 'Bearer {}'.format(token)})
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['projects'])

    def test_get_projects_by_user_id_without_authorization_headers(self):
        res = self.client().get('/api/projects')
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 401)

    def test_post_new_project_success(self):
        res = self.client().post('/api/projects', json=self.new_project , headers={'Authorization': 'Bearer {}'.format(token)})

        data = json.loads(res.data)
        print('post_new_project_data: ', data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['projects']) != 0)
        self.assertTrue(data['success'])

    def test_post_new_project_failure(self):
        res = self.client().post('/api/projects/1', json=self.new_project , headers={'Authorization': 'Bearer {}'.format(token)})

        data = json.loads(res.data)
        print('post_new_project_data: ', data)
        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])

    # test profile route
    def test_profile(self):
        res = self.client().get('/api/profile', headers={'Authorization': 'Bearer {}'.format(token)})
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['profile'])

    def test_profile_without_role_permission(self):
        res = self.client().get('/api/profile', headers={'Authorization': 'Bearer {}'.format(restricted_permission_token)})
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertFalse(data['success'])

    # def test_get_user_and_project_specific_workspaces(self)
    #     res = self.client().get()
        


if __name__ == "__main__":
    unittest.main()
