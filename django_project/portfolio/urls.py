from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),  # todas as URLs do PostViewSet ficam aqui
]

