from django.urls import path
from . import views

urlpatterns = [
    path('', views.vistaTexto, name='vista_texto'),
    path('t/<name>', views.vistaTemplate, name='vista_template'),
]