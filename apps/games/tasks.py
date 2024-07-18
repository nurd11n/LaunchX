import logging
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task
from decouple import config

logger = logging.getLogger(__name__)


@shared_task()
def application_send_mail(instance):
    to_emails = config('EMAILS')
    subject = f"Survey Response from {instance.fullname}"
    message = (
        f'phone_number: {instance.phone_number}\n'
        f'full_name: {instance.full_name}\n'
        f'game: {instance.game.title}'
        f'games_date: Real date {instance.game.date} -> Users Date {instance.date}\n'
        f'games_time: {instance.game.time}\n'
        f'games_max_people: {instance.game.max_people}\n'
        f'people_count: {instance.people_count}'
    )

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to=to_emails)
    email.send()
