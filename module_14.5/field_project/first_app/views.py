from django.shortcuts import render
from . forms import ContactForm

# Create your views here.


def home(request):
  return render(request, 'home.html')

def DjangoForm(request):
  form = ContactForm()
  return render(request, 'django_form.html', {'form' : form})