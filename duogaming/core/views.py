from django.shortcuts import render, redirect
from games.models import Categoria, Juego
from .forms import SignupForm
from django.contrib import messages
# Create your views here.

def index(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()


    return render(request, "core/index.html", {
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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm


@login_required
def modificar_usuario(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha modificado al usuario')
            return redirect('/')  # replace 'some_view' with your desired redirect view
        else:
            messages.error(request, 'Error al modificar los datos')
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'core/modificar.html', {'form': form})

