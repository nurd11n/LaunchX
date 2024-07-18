import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.settings')

app = Celery('config', backend='redis', broker="redis://redis:6379/0")
app.config_from_object('django.conf:settings', namespace='Celery')

app.autodiscover_tasks()
