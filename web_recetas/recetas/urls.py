from django.urls import path
from recetas.views import index, ingredientes, recetas, receta, nueva_receta



urlpatterns = [
    path('', index, name='index'),
    path('ingredientes/', ingredientes, name='ingredientes'),
    path('recetas/', recetas, name='recetas'),
    path('receta/<int:pk>', receta, name='receta'),
    path('nueva_receta/', nueva_receta, name='nueva_receta')
]