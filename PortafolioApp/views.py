from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Noticia, Categoria
from .forms import NoticiaForm,CategoriaForm

# Create your views here.

def renderHome(request):
    return render(request, 'PortafolioApp/home.html')

def renderLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
        else:
            return HttpResponse('Invalid login details')  # O maneja el error de alguna otra forma
    return render(request, 'login.html')

def renderRegister(request):
    return render(request, 'PortafolioApp/register.html')

def renderEncuestas(request):
    return render(request, 'PortafolioApp/encuestas.html')

def renderProductos(request):
    return render(request, 'PortafolioApp/productos.html')

def renderContacto(request):
    return render(request, 'PortafolioApp/contacto.html')

def renderCampanas(request):
    return render(request, 'PortafolioApp/campanas.html')

def renderQuienes(request):
    return render(request, 'PortafolioApp/quienes.html')

def renderFunciona(request):
    return render(request, 'PortafolioApp/funciona.html')

def renderSalud(request):
    return render(request, 'PortafolioApp/salud.html')

def renderPortalPago(request):
    return render(request, 'PortafolioApp/portal_pago.html')


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
    return render(request, 'PortafolioApp/listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'PortafolioApp/crear_categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'PortafolioApp/editar_categoria.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'PortafolioApp/eliminar_categoria.html', {'categoria': categoria})