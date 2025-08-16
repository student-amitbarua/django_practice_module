from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def courses(request):
#     return HttpResponse("This is my app/courses page.")
# def about(request):
#     return HttpResponse("this is my first app/about page")

# def home(request):
#     return HttpResponse('this is first app page.')


def home(request):
    return render(request, 'first_app/home.html')