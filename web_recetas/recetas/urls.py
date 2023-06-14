from django.urls import path
from recetas.views import index, ingredientes



urlpatterns = [
    path('', index, name='index'),
    path('ingredientes/', ingredientes, name='ingredientes'),
]