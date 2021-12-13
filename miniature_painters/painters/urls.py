from django.urls import path
from . import views

app_name = "painters"
urlpatterns = [
    path('', views.get_painters),
]
