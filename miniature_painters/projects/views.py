import re
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
from datetime import datetime
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


def get_unique_project(project_id):
    try:
        return Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404

def get_unique_comment(comment_id):
    try:
        return Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404

@api_view(['GET'])
@permission_classes([AllowAny])
def get_projects(request):
    projects = Project.objects.all().order_by('start_date')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_projects(request):
    if request.query_params.get('unique'):
        project = get_unique_project(request.query_params.get('projectId'))
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    else:
        projects = Project.objects.filter(user_id=request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'POST'])
@permission_classes([IsAuthenticated])
def update_user_projects(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, start_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        project = get_unique_project(data.project)
        serializer = ProjectSerializer(project, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments(request, project_id):
    comments = Comment.objects.filter(project_id=project_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['PUT','POST'])
@permission_classes([IsAuthenticated])
def update_comments(request, project_id):
    if request == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data)
        if serializer.is_valid():
            project = get_unique_project(project_id)
            serializer.save(project=project, user=request.user, posted=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request == 'PUT':
        data = JSONParser().parse(request)
        comment = get_unique_comment(data.commment)
        serializer = CommentSerializer(comment, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

