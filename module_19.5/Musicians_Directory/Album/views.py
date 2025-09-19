from django.shortcuts import render, redirect
from . import forms
from .import models
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

def add_album(request):
   if request.method == 'POST':
      album_form = forms.AlbumForm(request.POST)
      if album_form.is_valid(): 
         album_form.save() 
         return redirect('add _album')
     
   else: 
      album_form = forms.AlbumForm()


   return render(request, 'add_album.html', {'form' : album_form})


class AddAlbumView(CreateView):
   model = models.Album
   form_class =  forms.AlbumForm
   template_name = 'add_album.html'
   success_url = reverse_lazy('homepage')
