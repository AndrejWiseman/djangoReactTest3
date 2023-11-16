from .models import Film
from .serializers import FilmSerializer
from rest_framework import generics

class FilmListCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
