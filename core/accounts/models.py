from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    id = models.CharField(max_length=100, primary_key=True, default=str(uuid4()))

    def __str__(self):
        return self.username
