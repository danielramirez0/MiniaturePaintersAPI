from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserFollowingSerializer
from .models import *
from authentication.serializers import *
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from datetime import datetime
from django.conf import settings
from rest_framework.parsers import JSONParser
from django.apps import apps
User = get_user_model()


@api_view(["GET"])
@permission_classes([AllowAny])
def get_painters(request):
    painters = User.objects.all().order_by('date_joined').exclude(is_staff=True)
    serializer = UserSerializer(painters, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_unique_painter(request, painter_id):
    painter = User.objects.get(pk=painter_id)
    serializer = UserSerializer(painter)
    return Response(serializer.data)


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def follow_user(request, painter_id):
    if request.method == "POST":
        data = {'user': request.user.id, 'following': painter_id}
        serializer = UserFollowingSerializer(data=data)
        if serializer.is_valid():
            following = User.objects.get(pk=painter_id)
            serializer.save(user=request.user, following=following)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        following = UserFollowing.objects.filter(
            user_id=request.user.id, following_id=painter_id)
        serializer = UserFollowingSerializer(following, many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        try:
            record = UserFollowing.objects.filter(
                user=request.user.id, following=painter_id)
            record.delete()
        except UserFollowing.DoesNotExist:
            raise Http404
        return Response({}, status=status.HTTP_200_OK)
