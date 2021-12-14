from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import UserFollowing
from django.contrib.auth import get_user_model
User = get_user_model()



class UserFollowingSerializer(serializers.ModelSerializer):
    # user =  UserSerializer(read_only=True)
    # project = ProjectSerializer(read_only=True)
    class Meta:
        model = UserFollowing
        fields = ['id', 'user', 'following']