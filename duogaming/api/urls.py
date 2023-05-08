from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('juegos/', views.JuegoList.as_view(), name='juego-list'),
]
