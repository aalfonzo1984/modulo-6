from django.urls import path
from recetas.views import index, ingredientes, recetas, receta



urlpatterns = [
    path('', index, name='index'),
    path('ingredientes/', ingredientes, name='ingredientes'),
    path('recetas/', recetas, name='recetas'),
    path('receta/<int:pk>', receta, name='receta'),
]