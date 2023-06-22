from django.forms import *
from recetas.models import Ingrediente, Receta


class IngredienteForm(ModelForm):
    
    class Meta:
        model = Ingrediente
        fields = ['nombre','imagen']
        # para modificar el aspecto del widgets
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nuevo ingrediente',
                }
            ),
            'imagen': ClearableFileInput(
                attrs={'placeholder':'Seleccione una imagen',
                       'class':'form-group',
                }
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.upper()


class RecetaForm(ModelForm):
    class Meta:
        model= Receta
        fields = '__all__'