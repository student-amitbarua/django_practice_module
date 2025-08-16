from django.urls import path, include
from first_app import views

urlpatterns = [
    path('', views.home),
    path('django_form/', views.DjangoForm, name='submit_form')
]
