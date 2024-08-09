from django.conf import settings
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (RegistrationSerializer,
                          CustomAuthTokenSerializer,
                          CustomTokenObtainSerializer,
                          PasswordChangeSerializer,
                          ProfileSerializer)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
import jwt
from ...models import Profile
from ..utils import EmailThread

User = get_user_model()


class UserRegistration(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.data['email']
            data = {
                "email": email,
            }
            user_obj = get_object_or_404(User, email=email)
            token = self.get_token_for_user(user_obj=user_obj)

            email_obj = EmailMessage('email/active.tpl',
                                     {'user_name': "test", "token": token},
                                     "admin1@admin.com",
                                     to=[email])
            # Sending email through multithreading to speed up the process.
            EmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_token_for_user(self, user_obj):
        token = RefreshToken.for_user(user_obj)
        return str(token.access_token)


class CustomTokenObtainView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "email": user.email,
            "token": token.key,
            "id": user.pk,
            "password": user.password,
        })


class CustomTokenDiscardView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class ChangePasswordView(generics.GenericAPIView):
    model = User
    serializer_class = PasswordChangeSerializer

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.check_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "ok",
                "code": status.HTTP_200_OK,
                "message": "Password changed successfully.",
                "data": []
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user.id)
        return obj


class ConsoleEmailView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        to = request.user.email
        token = self.get_token_for_user(user_obj=request.user)
        email_obj = EmailMessage('email/active.tpl',
                                 {'user_name': "test", "token": token},
                                 "admin1@admin.com",
                                 to=[to])
        # Sending email through multithreading to speed up the process.
        EmailThread(email_obj).start()
        return Response({"details": "Mail sent"}, status.HTTP_200_OK)

    def get_token_for_user(self, user_obj):
        token = RefreshToken.for_user(user_obj)
        return str(token.access_token)


class ActivationApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, token, *args, **kwargs):
        token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        print(token['user_id'])
        return Response({"details": "Your account has been verified",}, status=status.HTTP_200_OK)
