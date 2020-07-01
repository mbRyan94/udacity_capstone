


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
# app = SourceFileLoader("app", "app.py").load_module()
# db = SourceFileLoader("module", "../db/module.py").load_module()
# Please create a new token before running the tests
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikhfb1J6RENzMTVoZXV4Ym9pWDd4SCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWUzNDRlMDFmYjhjMzAwMTQ3MTQxM2MiLCJhdWQiOlsiZnJlZXRpbWUiLCJodHRwczovL2ZzbmQyMDIwLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTM2Mzk2MzUsImV4cCI6MTU5MzY0NjgzNSwiYXpwIjoidk96YW9uanJmZmdQZGE3dUhOUTRxR3FySDRJdkV2aFUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6d29ya2l0ZW0iLCJnZXQ6cHJvZmlsZSIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3RzIiwiZ2V0OndvcmtpdGVtIiwiZ2V0OndvcmtpdGVtcyIsImdldDp3b3Jrc3BhY2UiLCJnZXQ6d29ya3NwYWNlcyIsIm9wZW5pZDplbWFpbCIsInBhdGNoOnByb2plY3QiLCJwYXRjaDp3b3JraXRlbSIsInBvc3Q6cHJvamVjdHMiLCJwb3N0OndvcmtpdGVtcyIsInBvc3Q6d29ya3NwYWNlcyJdfQ.hKvg-7sUPHOe0uW5aoIH8XAp9aJzl8RgOloXZhX-ODMJJRyHfY4lLAfdtS5gOJbLiLXOPb1aD4kUTVkb3KBjZWAeLsJw3AZU6036p7fOtKYCGdQBjO6io-dnmGgxjqO1Uke7uImEea1cvTpfQPivaQ9KhexvxNyj-WRaRKaROIbgqZ86dhZ68B7Xrwgmul15ROV4ZYszKhuP7ndo9um3iSuxXM8dGwgCuiY2i5P-EFyIHp7fz_q3LkIplVl9CRhOoxVJZcCNDtncayGmQMWB8AC6OuLSFCscMLHxvjtJQcKOw2qwvgLno4Lv0pU8PV8CZ1Fv6-CF4ex1iBABDtd3uA'


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
            "name": "Project #1",
            "description": "Client #1 - Biz and Marketing",
            "user_id": "5ee344e01fb8c3001471413c"
        }

    def test_get_projects_by_user_id(self):
        res = self.client().get('/api/projects', headers={'Authorization': 'Bearer {}'.format(token)})
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_projects_by_user_id_without_authorization_headers(self):
        res = self.client().get('/api/projects')
        data = json.loads(res.data)
        print('data: ', data)
        self.assertEqual(res.status_code, 401)
        


if __name__ == "__main__":
    unittest.main()
