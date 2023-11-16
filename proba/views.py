from django.shortcuts import render
from .models import Film
from .serializers import FilmSerializer
from rest_framework import generics



def front(request):
    context = {

    }
    return render(request, "index.html", context)



class FilmListCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


