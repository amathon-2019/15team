from django.db import models
from django.contrib.auth.models import User
import uuid


class Key(models.Model):
    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    count = models.IntegerField(default=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.api_key)

    def is_valid(self):
        if(self.count==0):
            return False
        else:
            return True
        
    def used(self):
        self.count -= 1
        self.save()
    
    def fill(self, count):
        self.count += count
        self.save()

class Coupon(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    api_key = models.ForeignKey(Key, on_delete=models.CASCADE)