

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', include('app.urls')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)