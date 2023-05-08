from django.shortcuts import render, redirect
from games.models import Categoria, Juego
from .forms import SignupForm
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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

