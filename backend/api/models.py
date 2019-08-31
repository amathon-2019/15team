from django.db import models
from django.contrib.auth.models import User
import uuid

class Key(models.Model):
    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)