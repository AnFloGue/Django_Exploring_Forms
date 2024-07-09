# Django_Exploring_Forms/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_01.urls')),
    path('home/', include('app_01.urls')),
    
    path('index/', include('app_01.urls')),
    path('app_01/', include('app_01.urls')),  # This line includes urls from app_01
    path('app_01/home/', include('app_01.urls')),  # This line includes urls from app_01
]