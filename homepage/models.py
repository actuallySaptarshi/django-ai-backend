from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    chats = models.IntegerField(null=True)
    promptsAnswered = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.name}"

class contact_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}    {self.email}"