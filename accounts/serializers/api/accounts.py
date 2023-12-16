import pdb

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from accounts.serializers.nested.profile import ProfileSerializer, ProfileUpdateSerializer

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
       style={'input_type': 'password'},
       write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже зарегистрирован.'
            )
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        validate_password(attrs['password'])
        if attrs['password'] != attrs['password2']:
            raise ParseError("Пароли не совпадают.")
        return attrs

    def validate_old_password(self, old_password):
        user = self.instance
        if not user.check_password(old_password):
            raise ParseError("Проверьте правильность текущего пароля.")
        return old_password

    def update(self, instance, validated_data):
        password = validated_data['password']
        instance.set_password(password)
        instance.save()
        return instance


# class ResetPasswordEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)


class MeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',
            'date_joined',
        )


class MeUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUpdateSerializer()
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile') if 'profile' in validated_data else None
        with transaction.atomic():
            instance = super().update(instance, validated_data)
            self._update_profile(instance.profile, profile_data)
        return instance

    def _update_profile(self, profile, data):
        profile_serializer = ProfileUpdateSerializer(
            instance=profile,
            data=data,
            partial=True,
        )
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()



