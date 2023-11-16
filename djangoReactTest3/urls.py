
from django.contrib import admin
from django.urls import path, include
from core.views import front

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('proba.urls')),

    path("", front, name="front"),
]
