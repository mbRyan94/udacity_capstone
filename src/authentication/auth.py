import json
import os
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import sys

AUTH_DOMAIN = os.getenv('AUTH_DOMAIN')
ALGORITHM = os.getenv('ALGORITHM')
API_AUDIENCE = os.getenv('API_AUDIENCE')


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    try:
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            raise AuthError({
                'status': 'no_authentication_header',
                'description': 'missing authentication header'
            }, 401)
        bearer_token = auth_header.split(' ')

        if bearer_token[0].lower() == 'bearer' and len(bearer_token) == 2:
            token = bearer_token[1]

            return token
        else:
            raise AuthError(
                {
                    'status': 'malformed_header',
                    'description': 'malformed header included'
                }, 401)
        return token
    except Exception:
        print(sys.exc_info())
        abort(401)


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'status': 'payload_without_permissions',
            'description': 'the payload does not have any permission attributes'
        }, 401)

    if permission not in payload['permissions']:
        raise AuthError({
            'status': 'invalid_permissions',
            'description': 'invalid permissions'
        }, 401)

    return True


def verify_decoded_jwt(token):
    rsa_keys = {}
    try:
        JWKS_file = urlopen(
            f'{AUTH_DOMAIN}.well-known/jwks.json')
    except Exception:
        print(sys.exc_info())

    jwks = json.loads(JWKS_file.read())

    jwks_kid = jwks['keys'][0]['kid']

    try:
        token_header = jwt.get_unverified_headers(token)
    except jwt.JWTError:
        raise AuthError({
            'status': 'unverifed_token_header_error',
            'description': 'Error getting unverified token headers'
        }, 401)

    token_kid = token_header['kid']
    if not token_kid:
        raise AuthError({
            'status': 'missing_token_kid',
            'description': 'token kid is missing'
        }, 401)

    if jwks_kid != token_kid:
        raise AuthError({
            'status': 'invalid_token_header',
            'description': 'token header is invalid'
        }, 401)

    for key in jwks['keys']:
        if (rsa_keys):
            break
        rsa_keys = {
            "kty": key['kty'],
            "use": key['use'],
            "n": key['n'],
            "e": key['e']
        }

    try:
        payload = jwt.decode(token, rsa_keys, algorithms=ALGORITHM,
                             issuer=AUTH_DOMAIN, audience=API_AUDIENCE)

        return payload

    except jwt.JWTError:
        raise AuthError({
            'status': 'invalid_signature',
            'description': 'invalid signature for decoding the token'
        }, 401)
    except jwt.JWTClaimsError:
        raise AuthError({
            'status': 'invalid_claims',
            'description': 'invalid claims for decoding the token'
        }, 401)
    except jwt.ExpiredSignatureError:
        raise AuthError({
            'status': 'expired_signature',
            'description': 'signature has expired'
        }, 401)


def require_auth(permission=""):
    def auth_decorator_function(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decoded_jwt(token)
                check_permissions(permission, payload)
                return func(payload, *args, **kwargs)
            except AuthError:
                abort(401)

        return func_wrapper
    return auth_decorator_function


def get_token_user_id(jwt_payload):
    subject = jwt_payload['sub']
    if not subject:
        return AuthError({
            'status': 'token_without_subject',
            'description': 'no user provided'
        }, 401)
    user_id = subject.split('|')[1]
    return user_id
