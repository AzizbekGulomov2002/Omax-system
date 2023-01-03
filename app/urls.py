from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ImportViewSet,MijozViewSet,BuyurtmaViewSet,ExportViewSet
router = DefaultRouter()
router.register('import', ImportViewSet)
router.register('export', ExportViewSet)
router.register('mijoz', MijozViewSet)
router.register('buyurtma', BuyurtmaViewSet)

urlpatterns = [ 
    path("", include(router.urls))
]