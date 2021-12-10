from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Progress)
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(WatchedProject)

