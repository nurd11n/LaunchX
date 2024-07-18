from decouple import config

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'  
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/signup/'
ACCOUNT_LOGIN_REDIRECT_URL = '/accounts/signup/'
SOCIALACCOUNT_LOGIN_ON_GET = True
# LOGOUT_REDIRECT_URL = '/accounts/email/'
RECT_URL = '/accounts/email/'
