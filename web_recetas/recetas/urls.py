from django.urls import path
from recetas.views import index, ingredientes, recetas



urlpatterns = [
    path('', index, name='index'),
    path('ingredientes/', ingredientes, name='ingredientes'),
    path('recetas/', recetas, name='recetas'),
]