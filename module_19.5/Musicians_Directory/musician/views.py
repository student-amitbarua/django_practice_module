from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .import forms 
from .import models 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView



# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musicians')
        
    else: 
        musician_form = forms.MusicianForm()

    return render(request, 'add_musicians.html', {'form' : musician_form})
    
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('add_musicians')
           
        

def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == "POST":
        musician_form= forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()

            return redirect('homepage')
        
    return render(request, 'add_musicians.html', {'form' : musician_form})


class EditMusicanView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musicians.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')




def delete_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()

    return redirect('homepage')


class DeleteMusicianView(DeleteView):
    model = models.Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'