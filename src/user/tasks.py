from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import User


@shared_task()
def send_welcome_email(user_id):
    try:
        user = User.objects.get(pk=user_id)
        subject = 'Welcome to library'
        message = f'Thank you for registering, {user.username}!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email)
    except Exception as e:
        pass
