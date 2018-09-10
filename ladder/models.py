from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'username']

class ErgPiece(models.Model):
    date = models.DateTimeField()
    time = models.TimeField()
    distance = models.IntegerField()
    email = models.ForeignKey(User, on_delete=models.CASCADE)
