import uuid
import warnings

from calendar import timegm
from datetime import datetime

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field

from rest_framework_jwt.settings import api_settings


jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


def decode_jwt(token):
    return jwt_decode_handler(token)


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )
    print(user, user.pk, type(user), user.groups.values_list('name', flat=True)[0])
    payload = {
        'user_id': user.pk,
        'username': username,
        'group': str(user.groups.values_list('name', flat=True)[0]),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload

