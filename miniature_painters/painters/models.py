from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class UserFollowing(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='following')
    following = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='followers')

    created = models.DateTimeField(auto_now_add=True)
