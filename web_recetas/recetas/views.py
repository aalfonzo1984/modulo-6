from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':  # Si el metodo de la request es POST se intenta guardar el ingrediente, caso  de que no se pueda guardar se returna el error del formulario
        try:
            form = IngredienteForm(request.POST, request.FILES)
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
    recetas = Receta.objects.all()  # Se muestran todas las recetas
    if request.method == 'GET':
        form = RecetaForm(request.GET)
        if form['nombre'].value():  # Busqueda por nombre de receta
            recetas = Receta.objects.filter(
                nombre__icontains=form['nombre'].value())  # Filtro a la BD, comparando si los registros contienen las palabras intgroducidas en el campo del formulario

        elif form['ingredientes'].value():  # Busqueda por los ingredientes de las recetas
            recetas = Receta.objects.filter(
                ingredientes__id__in=form['ingredientes'].value()).distinct()  # Filtro a la BD, escogiendo solamente las recetas que contengan los ingredientes seleccionados
            

    context = {'recetas': recetas, 'titulo': titulo, 'form': form}
    return render(request, 'recetas/recetas.html', context)


def receta(request, pk):
    receta = Receta.objects.get(id=pk)
    ultimas_recetas = Receta.objects.order_by('-id')[:3]
    titulo = receta.nombre
    context = {'receta': receta, 'titulo': titulo,
               'ultimas_recetas': ultimas_recetas}
    return render(request, 'recetas/receta.html', context)


def nueva_receta(request):

    titulo = 'Nueva Receta'
    if request.method == 'POST':
        try:
            form=NuevaRecetaForm(request.POST, request.FILES)
            if form.is_valid(): 
                form.save()
                # Agrega un mensaje flash para indicar que la receta se ha agregado con éxito
                messages.success(request, 'Receta agregada exitosamente.')
                return redirect('.')# Redirige a la página de recetas
        except:
            return form.errors
    else:
        form=NuevaRecetaForm()

    context = {'titulo':titulo, 'form':form}

    return render(request, 'recetas/nueva_receta.html', context)