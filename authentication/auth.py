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
            }, 403)
        bearer_token = auth_header.split(' ').lower()
        print('bearer_token: ', bearer_token)
        if bearer_token[0] == 'bearer' and bearer_token.len() != 2:
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
def verify_decoded_jwt(token):
    rsa_keys = {}
    try:
        JWKS_file = urlopen(
            'https://{}/.well-known/jwks.json'.format(AUTH_DOMAIN))
    except Exception:
        print(sys.exc_info())

    jwks = json.loads(JWKS_file.read())
    print('jwks: ', jwks)

    jwks_kid = jwks['keys'][0]['kid']
    print('jwks keyId: ', jwks_kid)
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

    for key in jwks['keys'][0]:
        rsa_keys = {
            "kid": key['kid'],
            "use": key['use'],
            "n": key['n'],
            "e": key['e']
        }
    print('rsa_keys: ', rsa_keys)

    try:
        payload = jwt.decode(token, rsa_keys, algorithms=ALGORITHM,
                             issuer=AUTH_DOMAIN, audience=API_AUDIENCE)

        print('payload: ', payload)
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


# require_auth wrapper
