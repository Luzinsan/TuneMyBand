from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, permissions, status, response, views

from accounts.models.profile import Profile
from accounts.serializers.api import accounts

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = accounts.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        request=accounts.ChangePasswordSerializer,
        summary='Смена пароля', tags=['Аутентификация & Авторизация']),
)
class ChangePasswordView(views.APIView):
    def post(self, request):
        user = request.user
        serializer = accounts.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(summary='Пользователь', tags=['Пользователи']),
    patch=extend_schema(summary='Частично обновить данные пользователя', tags=['Пользователи']),
)
class MeView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = accounts.MeSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return accounts.MeUpdateSerializer
        return accounts.MeSerializer

    def get_object(self):
        return self.request.user


