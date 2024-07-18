from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_code(email, activation_code):
    context = {
        'text_detail': 'Thank you for registration!',
        'email': email,
        'domain': 'http://localhost:8000',
        'activation_code': activation_code,

    }

    msg_html = render_to_string('email.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Account activation',
        message,
        'test@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False,
    )


def send_password(email, forgot_password_code):
    context = {
        'text_detail': 'Password recovery',
        'email': email,
        'domain': 'http://127.0.0.1:8000/',
        'forgot_password_code': forgot_password_code
    }
    message_html = render_to_string('lose_password.html', context)
    message = strip_tags(message_html)
    send_mail('Password recovery',
              message,
              'admin@gmail.com',
              [email],
              html_message=message_html,
              fail_silently=False
              )
