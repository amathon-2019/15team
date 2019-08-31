from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from . import models, serializers


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {
                    "user": serializers.UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "token": str(Token.objects.create(user=user)),
                }
            )
        return Response({'zz': 'zz'})


class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        try:
            token = Token.objects.get(user_id=user.id)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        return Response(
            {
                "token": str(token),
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


class KeyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        serializer = serializers.KeySerializer(models.Key.objects.filter(user=request.user), many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        key = models.Key.objects.create(user=request.user,api_key=request.data["k"], count=request.data["c"])
        content = {
            'user': str(key),  # `django.contrib.auth.User` instance.
        }
        return Response(content)


class MainView(APIView):

    def get(self, request, format=None):
        print(request)
        return Response()


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))
