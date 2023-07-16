from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name = 'inicio'),
    path('categoria', views.categoria , name = 'categoria'),
    path('autor', views.autor , name = 'autor'),
    path('articulo', views.articulo , name = 'articulo'),
    path('archivo', views.archivo , name = 'archivo')
]