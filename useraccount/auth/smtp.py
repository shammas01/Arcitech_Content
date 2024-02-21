from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def send_activation_email(user=None, email=None):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    subject = 'Activate your account'
    message = f'Please use the following link to activate your account:\nhttp://127.0.0.1:8000/users/activate/{uid}/{token}/'

    mail_subject = subject
    message = render_to_string(
        "user_activation.html", {"user": user, "message": message, "email": email}
    )
    to_email = email

    send_mail = EmailMessage(mail_subject, message, email, to=[to_email])
    send_mail.send()