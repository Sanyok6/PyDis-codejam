from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models

User = get_user_model()


class ReallyBadChessStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReallyBadChessStats
        fields = ('wins', 'losses', 'draws')


class MagicChessStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MagicChessStats
        fields = ('wins', 'losses', 'draws')


class UserStatsSerializer(serializers.ModelSerializer):
    really_bad_chess = ReallyBadChessStatsSerializer()
    magic_chess = MagicChessStatsSerializer()

    class Meta:
        model = models.UserStats
        fields = ('really_bad_chess', 'magic_chess')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, user_data):
        return User.objects.create_user(user_data['username'], password=user_data['password'])


class UserSerializer(serializers.ModelSerializer):
    password = None
    userstats = UserStatsSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_playing', 'userstats')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()