from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path('', views.get_projects),
    path('user/', views.get_user_projects),
    path('user/update/', views.update_user_projects),
    path('comments/<int:project_id>', views.get_comments),
    path('comments/update/<int:project_id>', views.update_comments),
    path('comments/<int:comment_id>/replies/', views.get_replies),
    path('comments/replies/update/<int:comment_id>', views.update_replies),
]