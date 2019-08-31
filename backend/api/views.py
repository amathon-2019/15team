from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from . import models, serializers
import secrets
from django.shortcuts import get_object_or_404



# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class KeyView(APIView):
    
    def get(self, request, format=None):
        serializer = serializers.KeySerializer(models.Key.objects.filter(user=request.user), many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        key = models.Key.objects.create(user=request.user, count=1000)
        content = {
            'user': key,  # `django.contrib.auth.User` instance.
        }
        return Response(content)


class MainView(APIView):

    def get(self, request, key, format=None):
        try:
            key = get_object_or_404(models.Key, api_key=key)
            key.count -= 1
            key.save()
            # do some job
            content = {
                'user': str(key),  # `django.contrib.auth.User` instance.
            }
            return Response(content)
        except:
            return Response({"error":"invalid key"})