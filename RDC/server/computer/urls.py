from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.intro, name="into"),
    path("devices/", views.all, name="devices")
]
