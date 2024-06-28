from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import UserRegistrationForm
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required

from PortafolioApp.models import Noticia,Categoria
from PortafolioApp.forms import NoticiaForm,CategoriaForm
# Create your views here.


def productos(request):
    return render(request, "productos.html")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Usuario registrado")
            return redirect("login")  # Redirige a la página de login o a donde prefieras
        else:
            messages.add_message(request=request, level=messages.WARNING, message="Error al registrar")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "signup.html", context)


def renderLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
        else:
            return HttpResponse('Invalid login details')  # Manejar el error de autenticación
    return render(request, 'PortafolioApp/home.html')  # Renderizar el formulario de login si el método no es POS


def Contacto(request):
    return render(request, 'PortafolioApp/contacto.html')


def Campanas(request):
    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'user_type': user_type,
    }
    return render(request, 'PortafolioApp/campanas.html', context)


def Home(request):
    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'user_type': user_type,
    }
    return render(request, 'PortafolioApp/home.html', context)

def returnHome(request):
    return render(request, 'PortafolioApp/home.html')


def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')  # Redirigir a la lista de noticias o donde prefieras
    else:
        form = NoticiaForm()

    context = {
        'form': form,
    }
    return render(request, 'PortafolioApp/crear_noticia.html', context)

def lista_noticias(request):
    noticias = Noticia.objects.all()
    context = {
        'noticias': noticias,
    }
    return render(request, 'PortafolioApp/listar_noticias.html', context)

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {
        'noticia': noticia,
    }
    return render(request, 'PortafolioApp/detalle_noticia.html', context)

def listar_categorias(request):
    categorias = Categoria.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'categorias': categorias,
        'user_type': user_type,
    }
    
    return render(request, 'PortafolioApp/listar_categorias.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()

    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'form': form,
        'user_type': user_type,
    }

    return render(request, 'PortafolioApp/crear_categoria.html', context)

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'form': form,
        'user_type': user_type,
    }

    return render(request, 'PortafolioApp/editar_categoria.html', context)

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')

    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'categoria': categoria,
        'user_type': user_type,
    }

    return render(request, 'PortafolioApp/eliminar_categoria.html', context)
