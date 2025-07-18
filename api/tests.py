from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email from Django',
    'Hello! This is a test message sent from your Django app.',
    settings.EMAIL_HOST_USER,  # Sender
    ['pirachanna0504@email.com'],  # Recipient (replace with your actual email)
    fail_silently=False,
)
