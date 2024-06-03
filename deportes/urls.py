from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria.html', views.galeria, name='galeria'),
    path('contenido.html',views.contenido, name='contenido'),
]
