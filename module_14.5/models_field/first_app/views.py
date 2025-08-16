from django.shortcuts import render
from first_app import models
# Create your views here.

def home(request):
    student = models.Student.objects.all()

    return render(request, 'home.html', {'data' : student})