from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

CELERY_BROKER_URL = "redis://redis:6379/0" #'redis://redis:6379/0'
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
REDIS_HOST = 'redis'
REDIS_PORT = '6379'