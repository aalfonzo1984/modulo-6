from django.shortcuts import render, redirect
from recetas.models import Ingrediente, Receta
from recetas.forms import *

# Create your views here.


def index(request):
    titulo = 'Home'
    # Traigo las ultimas 5 recetas guardadas
    recetas = Receta.objects.order_by('-id')[:5]
    context = {'titulo': titulo, 'recetas': recetas}
    return render(request, 'recetas/index.html', context)


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
    context = {'form': form, 'ingredientes': ingredientes, 'titulo': titulo}
    return render(request, 'recetas/ingredientes.html', context)


def recetas(request):
    
    titulo = 'Recetas'
    recetas = Receta.objects.all()
    if request.method == 'GET':
        form = RecetaForm(request.GET)
        if form['nombre'].value():
            recetas = Receta.objects.filter(nombre__icontains=form['nombre'].value())
            
        """ elif form['ingredientes'].value():
            recetas = Receta.objects.filter(ingredientes__icontains=form['ingredientes'].value()) """

    context = {'recetas': recetas, 'titulo': titulo, 'form':form}
    return render(request, 'recetas/recetas.html', context)


def receta(request, pk):
    receta = Receta.objects.get(id=pk)
    print(receta.ingredientes.all())
    ultimas_recetas = Receta.objects.order_by('-id')[:3]
    titulo = receta.nombre
    context = {'receta': receta, 'titulo': titulo,
               'ultimas_recetas': ultimas_recetas}
    return render(request, 'recetas/receta.html', context)
