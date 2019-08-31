from django.db import models
from django.contrib.auth.models import User


class Key(models.Model):
    api_key = models.TextField(max_length=100)
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)