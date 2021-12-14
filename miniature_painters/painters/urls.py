from django.urls import path
from . import views

app_name = "painters"
urlpatterns = [
    path('', views.get_painters),
    path('<int:painter_id>', views.get_unique_painter),
    path('follow/<int:painter_id>', views.follow_user),
    path('unfollow/<int:painter_id>', views.follow_user),
]
