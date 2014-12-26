
from django.core.mail import send_mail


def mail_it():
    send_mail('Subject here', 'Here is the message.', email_host,
              ['fo311@ic.ac.uk'], fail_silently=False)
