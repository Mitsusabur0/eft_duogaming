from django import forms
from django.core.exceptions import ValidationError
from .models import Juego, Categoria
from PIL import Image


def validate_square_image(image):
    img = Image.open(image)
    width, height = img.size
    if width != height:
        raise ValidationError('La imagen debe ser cuadrada.')
    
class NuevoJuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen',)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre del juego'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'placeholder': 'Descripción del juego'}))
    precio = forms.FloatField(label='Precio', widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'step': '0.01'}))
    imagen = forms.ImageField(validators=[validate_square_image], label='Imagen')

class EliminarJuegoForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria')
    juego = forms.ModelChoiceField(queryset=Juego.objects.all(), label='Juego')



