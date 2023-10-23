from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import (RegistrationSerializer, ActivationSerializer,
                         LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer,
                         ForgotPasswordCompleteSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Аккаунт успешно создан. На вашу почту был отправлен код активации.', status=201)


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response('Аккаунт успешно активирован!', status=200)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        token = Token.objects.filter(user=user).delete
        return Response('Вы успешно вышли из своего аккаунта')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен', status=200)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_verification_email()
        return Response('Вам был отправлено сообщение для восстановления пароля')


class ForgotPasswordCompleteView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен')