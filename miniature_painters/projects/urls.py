from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    # path('', views.Projects.as_view()),
    path('all/', views.get_all_projects),
    path('user/', views.user_projects)
]