from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    subject = 'Добро пожаловать!'
    message = f'Привет, {user.username}! Спасибо за регистрацию на нашем сайте.'
    from_email = 'your@example.com'
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email)
