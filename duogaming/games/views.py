from django.shortcuts import render
from .models import Juego, Categoria

# Create your views here.
def categoria(request, nombre_categoria):
    juegos = Juego.objects.all()
    categoria = Categoria.objects.get(nombre=nombre_categoria)

    return render(request, "games/categoria.html", {
        'categoria': categoria,
        'juegos': juegos,
    })






#  Cada categoria tiene que link a una pagina de la categoria
#  Luego, dentro de esta pagina, se itera los juegos
#  La iteración se implementa igual que la de las categorias en el index.html