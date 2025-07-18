from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

class ContactView(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        number = request.data.get("number")
        subject = request.data.get("subject") or "No Subject"
        message = request.data.get("message")

        contact = Contact(
            name=name,
            email=email,
            number=number,
            subject=subject,
            message=message
        )
        contact.save()

        full_message = f"""
        You received a new message from your portfolio contact form:

        Name: {name}
        Email: {email}
        Number: {number}
        Subject: {subject}

        Message:
        {message}
        """

        try:
            send_mail(
                subject=f"Portfolio Contact - {subject}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['pirachanna0504@gmail.com'], 
                fail_silently=False,
            )
            return Response({"success": True, "message": "Message received and email sent."})
        except Exception as e:
            return Response({"success": False, "message": "Message saved, but failed to send email.", "error": str(e)})
