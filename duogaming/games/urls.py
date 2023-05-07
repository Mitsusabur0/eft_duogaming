from django.urls import path
from . import views

urlpatterns = [
    path('<str:nombre_categoria>/', views.categoria, name='categoria'),
]



