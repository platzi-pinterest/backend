"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from pinterest.users.models import User
# from pinterest.rides.models import Ride

# Celery
from celery.decorators import task
# from celery.decorators import task, periodic_task

# Utilities
import jwt

# import time
from datetime import timedelta


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Welcome @{}! Verify your account to start using Event Up'.format(user.username)
    from_email = 'Event Up <noreply@pinterest.codes>'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user, 'domain': settings.MAIN_DOMAIN[0]}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


# Can be with cron tab rules (cronjobs * * * * 10)
# @periodic_task(name='disable_finished_rides', run_every=timedelta(minutes=20))
# def disable_finished_rides():
#     """Disable finished rides."""
#     now = timezone.now()
#     offset = now + timedelta(minutes=20)

#     # Update rides that have already finished
#     rides = Ride.objects.filter(
#         arrival_date__gte=now,
#         arrival_date__lte=offset,
#         is_active=True
#     )
#     rides.update(is_active=False)
