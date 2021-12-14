from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import PainterFollower
from django.contrib.auth import get_user_model
User = get_user_model()



class PainterFollwerSerializer(serializers.ModelSerializer):
    # user =  UserSerializer(read_only=True)
    # project = ProjectSerializer(read_only=True)
    class Meta:
        model = PainterFollower
        fields = ['id', 'user', 'following']