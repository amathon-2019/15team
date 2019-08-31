from rest_framework import serializers
from . import models

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Key
        fields = '__all__'