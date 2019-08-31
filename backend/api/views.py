from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from backend.manage import models, serializers
from backend.manage.models import Key,Coupon



class CouponView(APIView):

    def get(self, request, key):
        serializer = serializers.CouponSerializer(models.Coupon.objects.filter(api_key = key), many=True)
        return Response(data=serializer.data)
        
    #generate coupon    
    def post(self, request, key):
        _key = Key.objects.get(api_key = key)
        coupon = Coupon.objects.create(api_key = _key)
        return Response({'coupon':str(coupon)})

    #use and delete coupon
    def delete(self, request, key):
        try:
            _key = Key.objects.get(api_key = key)
            coupon = Coupon.objects.filter(api_key = _key)[0]
            coupon.delete()
            return Response({'rslt':"succ"})
        except:
            return Response({'rslt':"fail"})