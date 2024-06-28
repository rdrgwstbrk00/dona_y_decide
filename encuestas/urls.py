from django.urls import path
from .views import crear_encuesta, ver_encuestas, responder_encuesta,donar_producto,productos_donados,eliminar_producto_donado,eliminar_encuesta

urlpatterns = [
    path('crear/', crear_encuesta, name='crear_encuesta'),
    path('ver/', ver_encuestas, name='ver_encuestas'),
    path('responder/<int:encuesta_id>/', responder_encuesta, name='responder_encuesta'),
    path('donar_producto/', donar_producto, name='donar_producto'),
    path('productos_donados/', productos_donados, name='productos_donados'),
    path('productos_donados/eliminar/<int:pk>/', eliminar_producto_donado, name='eliminar_producto_donado'),
    path('encuestas/eliminar/<int:pk>/', eliminar_encuesta, name='eliminar_encuesta'),
    
]
