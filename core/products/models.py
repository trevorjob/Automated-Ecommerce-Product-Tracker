from uuid import uuid4

from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Product(models.Model):
    id = models.CharField(
        max_length=50, primary_key=True, unique=True, default=str(uuid4())
    )
    result = models.JSONField(null=True)
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
