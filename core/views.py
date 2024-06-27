from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import UserRegistrationForm
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required

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
    return render(request, 'PortafolioApp/home.html')  # Renderizar el formulario de login si el método no es POST


def Contacto(request):
    return render(request, 'PortafolioApp/contacto.html')


def Campanas(request):
    return render(request, 'PortafolioApp/campanas.html')


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


