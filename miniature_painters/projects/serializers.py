from django.db.models import fields
from rest_framework import serializers
from .models import *
# from authentication.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name']


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'status']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'user_id', 'game', 'start_date',
                  'progress', 'name', 'likes', 'description']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'posted']


class ProjectPostSerializer(serializers.ModelSerializer):
    # user =  UserSerializer(read_only=True)
    # project = ProjectSerializer(read_only=True)
    class Meta:
        model = WatchedProject
        fields = ['id', 'project', 'post']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'body', 'posted', 'user_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'body', 'posted', 'user_id']

# class CommentSerializer(serializers.ModelSerializer):
#     replies = ReplySerializer(many=True, read_only=True)
#     class Meta:
#         model = Comment
#         fields = ['id', 'project', 'body', 'replies']

#     def create(self, validated_data):
#         replies_data = validated_data.pop('replies')
#         comment = Comment.objects.create(**validated_data)
#         for reply_data in replies_data:
#             Reply.objects.create(comment=comment, **reply_data)
#         return comment

# class UserProjectSerializer(serializers.ModelSerializer):
#     projects = ProjectSerializer(many=True, read_only=True)

#     class Meta:
#         model = UserProject
#         fields = ['id', 'user', 'projects']


class WatchedProjectSerializer(serializers.ModelSerializer):
    # user =  UserSerializer(read_only=True)
    # project = ProjectSerializer(read_only=True)
    class Meta:
        model = WatchedProject
        fields = ['id', 'user', 'project']
