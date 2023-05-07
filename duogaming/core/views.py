from django.shortcuts import render
from games.models import Categoria, Juego
# Create your views here.

def index(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()


    return render(request, "core/index.html", {
        # diccionario que pasa las listas creadas anteriormente 
        # como parameters al render
        'categorias': categorias,
        'juegos': juegos,
    })



