import datetime

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',


    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly', # default je IsAuthenticated, ReadOnly je dodato
    ],
    'DEFAULT_PAGINATION_CLASS': 'nemanjaapi.restconf.pagination.NEMANJAAPIPagination',
    'DEFAULT_FILTER_BACKENDS': (
    	'rest_framework.filters.SearchFilter', # dodat search rucno
    	'rest_framework.filters.OrderingFilter' # dodat filter rucno
    	),
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',
}


JWT_AUTH = {
'JWT_ENCODE_HANDLER':
'rest_framework_jwt.utils.jwt_encode_handler',

'JWT_DECODE_HANDLER':
'rest_framework_jwt.utils.jwt_decode_handler',

'JWT_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_payload_handler',

'JWT_PAYLOAD_GET_USER_ID_HANDLER':
'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

'JWT_RESPONSE_PAYLOAD_HANDLER':
#'rest_framework_jwt.utils.jwt_response_payload_handler',
'accounts.api.utils.jwt_response_payload_handler',


# 'JWT_SECRET_KEY': settings.SECRET_KEY,
# 'JWT_GET_USER_SECRET_KEY': None,
# 'JWT_PUBLIC_KEY': None,
# 'JWT_PRIVATE_KEY': None,
# 'JWT_ALGORITHM': 'HS256',
# 'JWT_VERIFY': True,
# 'JWT_VERIFY_EXPIRATION': True,
# 'JWT_LEEWAY': 0,
# 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
# 'JWT_AUDIENCE': None,
# 'JWT_ISSUER': None,

'JWT_ALLOW_REFRESH': True,
'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7), # posle uspesnog logovanja, nakon 7 dana istice token

'JWT_AUTH_HEADER_PREFIX': 'JWT', # Autorizacija: JWT <token>
'JWT_AUTH_COOKIE': None
}
