from django.forms import *
from recetas.models import Ingrediente, Receta


class IngredienteForm(ModelForm):

    class Meta:
        model = Ingrediente
        fields = ['nombre', 'imagen']
        # para modificar el aspecto del widgets
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nuevo ingrediente',
                }
            ),
            'imagen': ClearableFileInput(
                attrs={'placeholder': 'Seleccione una imagen',
                       'class': 'form-group',
                       }
            ),
        }

    def clean_nombre(self):
        """Funcion que recibe el nombre del ingrediente y lo returna en mayusuclas para ser guardado"""
        nombre = self.cleaned_data['nombre']
        return nombre.upper()


class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        widgets={
            'ingredientes':CheckboxSelectMultiple(
                attrs={
                    'type':'checkbox'
                }
            ),
        }


class NuevaRecetaForm(models.ModelForm):
    """ Formulario para nueva receta """
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la receta'
                }
            ),
            'ingredientes':CheckboxSelectMultiple(
                attrs={
                    'type':'checkbox'
                }
            ),
            'descripcion':TextInput(
                attrs={
                    'placeholder':'Escriba breve descripción de la receta'
                }
            ),'imagen': ClearableFileInput(
                attrs={'placeholder': 'Seleccione una imagen',
                       'class': 'form-group',
                       }
            ),
        }
