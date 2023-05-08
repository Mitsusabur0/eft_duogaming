from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Juego, Categoria
from .forms import NuevoJuegoForm, EliminarJuegoForm

def user_in_juego_permisos(user):
    if user.is_superuser:
        return True
    return user.groups.filter(name='juego_permisos').exists()

# Create your views here.
def categoria(request, nombre_categoria):
    juegos = Juego.objects.all()
    categoria = Categoria.objects.get(nombre=nombre_categoria)

    return render(request, "games/categoria.html", {
        'categoria': categoria,
        'juegos': juegos,
    })


@login_required
@user_passes_test(user_in_juego_permisos)
def nuevo_juego(request):
    if request.method == 'POST':
        form = NuevoJuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego guardado exitosamente')
            return redirect('/')
        else:
            messages.error(request, 'No se pudo guardar el juego. Por favor, corrija los errores en el formulario.')
    else:
        form = NuevoJuegoForm()

    return render(request, 'games/form.html', {
        'form': form,
        'title': 'Agregar Juego',
    })


@login_required
@user_passes_test(user_in_juego_permisos)
def eliminar_juego(request):
    if request.method == 'POST':
        form = EliminarJuegoForm(request.POST)
        if form.is_valid():
            juego = form.cleaned_data['juego']
            juego.delete()
            messages.success(request, 'Juego eliminado exitosamente.')
            return redirect('games:eliminar_juego')
    else:
        form = EliminarJuegoForm()

    return render(request, 'games/form_eliminar.html', {
        'form': form,
        'title': 'Eliminar Juego',
    })


