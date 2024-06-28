from django.urls import path
from .views import signup, productos,Campanas,Contacto,Home,returnHome


urlpatterns = [
    path('', signup, name="signup"),
    path('productos',productos,name="productos"),
    
    path('campanas',Campanas,name="campanas"),
    path('contacto',Contacto,name="contacto"),
    path('home',Home,name="home"),
    path('returnHome',returnHome,name="returnHome"),

]