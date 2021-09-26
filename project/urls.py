
from django.contrib import admin
from django.urls import path
from app.views import  home, form, create, view,  edit, update, delete, formPacotes, createPacotes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('createPacotes/', createPacotes, name='createPacotes'),
    path('formPacotes/', formPacotes, name='formPacotes'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete')
]
