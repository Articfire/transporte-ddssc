from django.urls import path
from . import views

urlpatterns = [
    path('solicitud_transporte', views.solicitud_transporte, name='solicitud_transporte'),
    path('catalago', views.catalago, name='catalago'),
    path('agenda', views.agenda, name='agenda'),
    path('notificacion', views.notificacion, name='notificacion'),
    path('asignacion', views.asignacion, name='asignacion'),
    path('firma', views.firma, name='firma'),
    path('api', views.api_documentacion, name='api_documentacion'),
    path('api/disponibilidad', views.api_disponibilidad, name='api_disponibilidad'),
    path('api/catalago', views.api_catalago, name='api_catalago'),
    path('api/catalago/<int:catalago_id>', views.api_catalago_filtro, name='api_catalago_filtro'),

]