from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from . import models, serializers
from rest_framework import status




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
        body = {"message": "Input doesn't valid for model"}
        return Response(body, status=status.HTTP_400_BAD_REQUEST)


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
        try:
            serializer = serializers.KeySerializer(models.Key.objects.get(user=request.user))
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        try:
            count = request.data["count"]
            key = models.Key.objects.create(user=request.user, count=count)
            serializer = serializers.KeySerializer(key)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        try:
            count = request.data["count"]
            key = models.Key.objects.get(user=request.user)
            key.fill(count)
            serializer = serializers.KeySerializer(key)
            return Response(data=serializer.data)
        except:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
