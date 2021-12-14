from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
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