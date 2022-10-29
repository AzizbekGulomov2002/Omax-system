from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ZakasViewSet
router = DefaultRouter()
router.register('zakas', ZakasViewSet)

urlpatterns = [ 
    path("", include(router.urls))
]