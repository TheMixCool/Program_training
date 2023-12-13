from django.urls import path
from . import views

urlpatterns = [
    path('', views.string_to_video, name='string_to_video'),
]
