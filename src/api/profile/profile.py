from flask import abort, jsonify, request
from flask_restful import Resource
import sys
import os
import requests

from src.authentication.auth import require_auth, AuthError, \
    get_token_auth_header


class Profile(Resource):
    method_decorators = [require_auth('get:profile')]

    def get(self, jwt_payload):
        try:
            token = get_token_auth_header()

            auth_domain = os.getenv('AUTH_DOMAIN')
            req_url = f'{auth_domain}userinfo'
            headers = {'Authorization': f'Bearer {token}'}

            profile = requests.get(req_url, headers=headers)

            if not profile:
                raise AuthError({
                    'status': 'unauthorized_fetch_profile',
                    'description': 'fetching the profile failed'
                }, 401)
            json_profile = profile.json()

            return {
                'success': True,
                'profile': json_profile
            }
        except AuthError:
            abort(401)
        except requests.exceptions.RequestException:
            print(sys.exc_info())
            abort(400)
