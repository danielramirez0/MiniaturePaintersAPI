from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    progress = models.ForeignKey(
        'Progress', max_length=20, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)


class Progress(models.Model):
    status = models.CharField(max_length=20)


class Game(models.Model):
    name = models.CharField(max_length=50)


class Comment(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted = models.DateField(blank=True, null=True)
    body = models.CharField(max_length=500)


class Reply(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    body = models.CharField(max_length=250)


# class UserProject(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)


class WatchedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
