from django.db import models
from django.contrib.auth.models import User
import uuid

class Key(models.Model):
    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    count = models.IntegerField(default=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_valid(self):
        if(self.count==0):
            return False
        else:
            return True
        
    def used(self):
        self.count -= 1
        self.save()