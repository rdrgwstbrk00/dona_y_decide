from django.urls import path
from .views import signup, productos,Campanas,Contacto,Home,returnHome,listar_categorias,crear_categoria,editar_categoria,eliminar_categoria


urlpatterns = [
    path('', signup, name="signup"),
    path('productos',productos,name="productos"),
    path('campanas',Campanas,name="campanas"),
    path('contacto',Contacto,name="contacto"),
    path('home',Home,name="home"),
    path('returnHome',returnHome,name="returnHome"),
    path('listar_categorias/',listar_categorias, name='listar_categorias'),
    path('crear_categoria/',crear_categoria, name='crear_categoria'),
    path('editar_categoria/',editar_categoria, name='editar_categoria'),
    path('eliminar_categoria/',eliminar_categoria, name='eliminar_categoria'),
]