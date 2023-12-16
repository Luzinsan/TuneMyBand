from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models.profile import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'birthday',
            'sex',
            'skills',
            'genres',
            'photo',
            'about',
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'birthday',
            'sex',
            # 'skills',
            # 'genres',
            'photo',
            'about',
        )
