from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


class Notesmodel(models.Model):

    id = models.AutoField(primary_key=True)
    title = encrypt(models.TextField(max_length=50, blank=False))
    description = encrypt(models.TextField(max_length=500, blank=False))
    category = encrypt(models.TextField(max_length=20, blank=False))
    due_date = encrypt(models.DateField())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)

