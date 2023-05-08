from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('nuevo/', views.nuevo_juego, name='nuevo'),
    path('eliminar/', views.eliminar_juego, name='eliminar_juego'),

    path('<str:nombre_categoria>/', views.categoria, name='categoria'),
]



