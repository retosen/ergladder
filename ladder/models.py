from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ['date_of_birth']
