# async_project/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.timer_view),  # troquei hello por timer
]
