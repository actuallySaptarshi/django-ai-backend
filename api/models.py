from django.db import models

# Create your models here.
class guestChats(models.Model):
    chats = models.JSONField()