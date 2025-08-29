from django.urls import path
from django.contrib import admin
from django.urls import path
from core import views   # mudou de main -> core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post/', views.home, name='post'),
]

