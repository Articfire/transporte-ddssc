from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitud_transporte, name='solicitud_transporte'),
    path('pago', views.pago, name='pago'),
    path('agenda', views.agenda, name='agenda'),
    path('asignacion', views.asignacion, name='asignacion'),
    path('firma', views.firma, name='firma'),
    path('api', views.api_agenda, name='api_agenida'),
]