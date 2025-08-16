# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("this is home page")

# def contact(request):
#     return HttpResponse("this is contact page")

from django.shortcuts import render

def index(request):
    return render(request,'index.html')