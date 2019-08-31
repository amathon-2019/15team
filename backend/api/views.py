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

def calcBMR(sex, weight, height, age):
    if sex == "m":
        return 655 + (9.6*weight) + (1.8*height) - (4.7*age)
    else:
        66 + (13.7*weight) + (5*height) - (6.8*age)



class KeyView(APIView):
    
    def get(self, request, format=None):
        serializer = serializers.KeySerializer(models.Key.objects.filter(user=request.user), many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        key = models.Key.objects.create(user=request.user)
        return Response({"user":key})


class myAPI(APIView):

    def get(self, request, key, format=None):
        try:
            key = get_object_or_404(models.Key, api_key=key)
            return Response({"count":key.count})
        except:
            return Response({"error":"invalid key"})
    
    def post(self, reqeust, key, format=None):

        key = get_object_or_404(models.Key, api_key=key)
        if key.is_valid():
            data = reqeust.data
            BMR = calcBMR(data["sex"], data["weight"],data["height"],data["age"])
            key.used()
            return Response({"BMR" : f' 숨만 쉬고 있어도 빅맥 {BMR//500}개까지는 살이 안찝니다.'})
        else: 
            return Response({"error":"count 0"})
