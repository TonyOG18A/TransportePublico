from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Ruta2A/', views.Ruta2A, name="Ruta2A")
]