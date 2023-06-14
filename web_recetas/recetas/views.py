from django.shortcuts import render, redirect
from recetas.models import Ingrediente, Receta
from recetas.forms import *

# Create your views here.


def index(request):
    titulo = 'Home'
    recetas = Receta.objects.all()
    return render(request, 'recetas/index.html', {'titulo': titulo, 'recetas': recetas})


def ingredientes(request):
    titulo = 'Ingredientes'
    ingredientes = Ingrediente.objects.all()
    if request.method == 'POST':
        try:
            form = IngredienteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('.')
        except:
            return form.errors

    else:
        form = IngredienteForm()

    return render(request, 'recetas/ingredientes.html', {'form': form, 'ingredientes': ingredientes, 'titulo': titulo})


def recetas(request):
    pass