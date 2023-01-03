from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ImportViewSet,MijozViewSet,BuyurtmaViewSet,ExportViewSet,HodimViewSet
router = DefaultRouter()
router.register('import', ImportViewSet)
router.register('export', ExportViewSet)
router.register('mijoz', MijozViewSet)
router.register('buyurtma', BuyurtmaViewSet)
router.register('hodim', HodimViewSet)

urlpatterns = [ 
    path("", include(router.urls))
]