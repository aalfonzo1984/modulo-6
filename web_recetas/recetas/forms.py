from django.forms import *
from recetas.models import Ingrediente


class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre']
        # para modificar el aspecto del widgets
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nuevo ingrediente',
                }
            )
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.upper()