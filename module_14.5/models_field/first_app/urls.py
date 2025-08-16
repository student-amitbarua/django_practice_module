from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home, name='homepage'),
    # path('delete/', views.delete_student, name='delete_student'),


]
