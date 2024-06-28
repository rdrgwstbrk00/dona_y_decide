from django.contrib import admin
from django.urls import path
from PortafolioApp.views import (
    renderHome, renderLogin, renderRegister, renderEncuestas,
    renderProductos, renderCampanas, renderContacto, renderQuienes,
    renderFunciona, renderSalud, crear_noticia, lista_noticias, 
    detalle_noticia, renderPortalPago
)
from core.views import Home
from encuestas.views import ver_encuestas, crear_encuesta, donar_producto, productos_donados
from . import views

urlpatterns = [
    path('home/', Home, name='home'),
    path('', renderHome, name='index'),
    path('register/', renderRegister, name='register'),
    path('portal_pago/', renderPortalPago, name='portal_pago'),
    path('encuestas/', renderEncuestas, name='encuestas'),
    path('productos/', renderProductos, name='productos'),
    path('campanas/', renderCampanas, name='campanas'),
    path('contacto/', renderContacto, name='contacto'),
    path('funciona/', renderFunciona, name='funciona'),
    path('salud/', renderSalud, name='salud'),
    path('donar_producto/', donar_producto, name='donar_producto'),
    path('ver/', ver_encuestas, name='ver_encuestas'),
    path('crear/', crear_encuesta, name='crear_encuesta'),
    path('productos_donados/', productos_donados, name='productos_donados'),
    path('crear_noticia/', crear_noticia, name='crear_noticia'),
    path('noticias/', lista_noticias, name='lista_noticias'),
    path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
]
