from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('mahasiswa/', include('mahasiswa.urls', namespace='mahasiswa')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('index/', dashboard, name='dashboard'),
]
