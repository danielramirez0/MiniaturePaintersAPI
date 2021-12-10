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
    # game = GameSerializer(read_only=True)
    # progress = ProgressSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'user', 'game', 'progress', 'name', 'likes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'body']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'project', 'body']

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