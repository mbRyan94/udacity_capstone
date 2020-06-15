import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import sys

AUTH_DOMAIN = 'fsnd2020.eu.auth0.com'
ALGORITHM = ['RSA256']
API_AUDIENCE = 'freetime'

# AuthError Exception


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# get_token_auth_header()
def get_token_auth_header():
    try:
        auth_header = request.headers.get('Authorization')
        print('auth_header: ', auth_header)
        if not auth_header:
            raise AuthError({
                'status': 'no_authentication_header',
                'description': 'missing authentication header'
            })
        bearer_token = auth_header.split(' ').lower()
        print('bearer_token: ', bearer_token)
        if bearer_token[0] == 'bearer':
            token = bearer_token[1]
        else:
            raise AuthError(
                {
                    'status': 'malformed_header',
                    'description': 'malformed header included'
                }, 403)
        return token
    except Exception:
        print(sys.exc_info())
        abort(401)


# check_permission(permission, payload)


# verify_decoded_jwt(token)

# require_auth wrapper
