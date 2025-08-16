<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.

def about(request):
   return render(request, 'navigation/about.html')

def contact(request):
=======
from django.shortcuts import render

# Create your views here.

def about(request):
   return render(request, 'navigation/about.html')

def contact(request):
>>>>>>> 741be0a09bad4a3df1d384bc6727a5b370486811
    return render(request, 'navigation/contact.html')