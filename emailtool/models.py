from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
class Survey(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    def __str__(self):
        return f"Survey from {self.name}"
from django.db import models
# class AudienceMember(models.Model):
#     email = models.EmailField()
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     address = models.TextField(blank=True)
#     phone = models.CharField(max_length=20, blank=True)
#     birthday = models.DateField(blank=True, null=True)
#     is_subscribed = models.BooleanField(default=True)
#     def __str__(self):
#         return self.email
class Audience(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} <{self.email}>"
 # emailtool/models.py
class Contact(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email_marketing = models.BooleanField(default=True, help_text='Agrees to receive email marketing')
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
#tages
# from django.db import models
# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
from django.db import models
class Campaign(models.Model):
    # your model fields here
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models
class EmailRecipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} <{self.email}>"
from django.db import models
class LinkButton(models.Model):
    TYPE_CHOICES = [
        ('web', 'Web'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    url = models.URLField()
    new_tab = models.BooleanField(default=False)
    def __str__(self):
        return self.url
from django.db import models
class Campaign(models.Model):
    title = models.CharField(max_length=200, default='New Campaign')
    status = models.CharField(max_length=50, choices=[('Sent', 'Sent'), ('Scheduled', 'Scheduled')], default='Scheduled')
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=50, choices=[('email', 'Email'), ('social', 'Social')], default='email')
    folder = models.CharField(max_length=50, choices=[('Welcome', 'Welcome'), ('Product', 'Product')], default='Welcome')
    def __str__(self):
        return self.title
from django.db import models
class SentEmail(models.Model):
    recipient_name = models.CharField(max_length=100)
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.subject} to {self.recipient_email}"
class AddContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


        from django.db import models
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    def __str__(self):
        return self.name