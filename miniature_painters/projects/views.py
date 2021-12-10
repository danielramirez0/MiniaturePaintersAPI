from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from datetime import date
from django.conf import settings
from rest_framework.parsers import JSONParser
from django.apps import apps

# class Projects(APIView):
#     '''CRUD for projects'''

#     permission_classes = [AllowAny]

#     def get(self, request):
#         '''Standard get request for projects'''
#         projects = Project.objects.all().order_by("date")
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         '''Add a new project'''
#         data = JSONParser().parse(request)
#         serializer = ProjectSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_projects(request):
    projects = Project.objects.all().order_by('date')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_projects(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, game=request.data.game,
                            progress=request.data.progress)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        projects = Project.objects.filter(user_id=request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
