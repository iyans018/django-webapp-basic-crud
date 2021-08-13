from django.urls import path

from .views import *

app_name = 'mahasiswa'
urlpatterns = [
    path('', mahasiswa, name='index'),
    path('create/', create, name='create'),
    path('update/<str:updateId>', update, name='update'),
    path('delete/<str:deleteId>', delete, name='delete'),
]
