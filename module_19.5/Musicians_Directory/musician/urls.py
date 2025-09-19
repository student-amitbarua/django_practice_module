from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    # path('add/', views.add_musician, name='add_musicians'),
    path('add/', views.AddMusicianCreateView.as_view(), name='add_musicians'),
    # path('edit/<int:id>', views.edit_musician, name= 'edit_musician'),
    path('edit/<int:id>', views.EditMusicanView.as_view(), name= 'edit_musician'),
    # path('delete/<int:id>', views.delete_musician, name='delete_musician')
    path('delete/<int:id>', views.DeleteMusicianView.as_view(), name='delete_musician')
]
