# backend/api/models.py

from mongoengine import Document, StringField, EmailField

class Contact(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    number = StringField(required=True)
    subject = StringField(required=True)
    message = StringField(required=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
