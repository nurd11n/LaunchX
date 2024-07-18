from config.celery import app
from .utils import send_activation_code, send_password


@app.task
def send_password_celery(email, forgot_password_code):
    send_password(email, forgot_password_code)


@app.task
def send_activation_code_celery(email, activation_code):
    send_activation_code(email, activation_code)