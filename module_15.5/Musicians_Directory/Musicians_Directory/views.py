from django.shortcuts import render
from musician.models import Musician
from Album.models import Album

def home(request):

    data = Musician.objects.all()

    info = Album.objects.all()

    

    return render(request, 'home.html', {'data' : data, 'info' : info})