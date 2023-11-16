from django.urls import path
from . import views

urlpatterns = [
    path('api/film/', views.FilmListCreate.as_view()),

]
