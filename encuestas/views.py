from django.shortcuts import render, redirect, get_object_or_404
from .models import Encuesta, ResultadoEncuesta,ProductoDonado
from .forms import EncuestaForm, ResultadoEncuestaForm,ProductoDonadoForm
from core.models import Profile
def crear_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_encuestas')
    else:
        form = EncuestaForm()
    return render(request, 'crear_encuesta.html', {'form': form})

def ver_encuestas(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'ver_encuestas.html', {'encuestas': encuestas})

def responder_encuesta(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, id_encuesta=encuesta_id)
    
    if request.method == 'POST':
        form = ResultadoEncuestaForm(request.POST)
        if form.is_valid():
            resultado = form.save(commit=False)
            resultado.encuesta = encuesta
            resultado.save()
            return redirect('ver_encuestas')
    else:
        form = ResultadoEncuestaForm()
    
    return render(request, 'responder_encuesta.html', {'form': form, 'encuesta': encuesta})


def donar_producto(request):
    encuestas = Encuesta.objects.filter(activa=True)  # Filtrar solo encuestas activas

    if request.method == 'POST':
        form_encuesta = ResultadoEncuestaForm(request.POST, request.FILES)
        form_producto = ProductoDonadoForm(request.POST, request.FILES)

        if form_encuesta.is_valid() and form_producto.is_valid():
            # Guardar resultados de la encuesta para todas las encuestas activas
            for encuesta in encuestas:
                resultado = form_encuesta.save(commit=False)
                resultado.encuesta = encuesta  # Asignar la encuesta actual al resultado
                resultado.save()

            # Guardar el producto donado
            producto_donado = form_producto.save(commit=False)
            producto_donado.save()

            # Redirigir a alguna página de éxito o a la misma página
            return redirect('donar_producto')  # Ajusta esto a la página adecuada

    else:
        form_encuesta = ResultadoEncuestaForm()
        form_producto = ProductoDonadoForm()

    return render(request, 'donar_producto.html', {'encuestas': encuestas, 'form_encuesta': form_encuesta, 'form_producto': form_producto})

def productos_donados(request):
    productos = ProductoDonado.objects.all()
    try:
        profile = Profile.objects.get(user=request.user)
        user_type = profile.user_type
    except Profile.DoesNotExist:
        user_type = None  # Manejar el caso donde no se encuentre el perfil

    context = {
        'productos': productos,
        'user_type': user_type,
    }  # Obtener todos los productos donados
    return render(request, 'productos_donados.html',context)

def eliminar_producto_donado(request, pk):
    # Obtén la instancia del producto donado que se desea eliminar
    producto_donado = get_object_or_404(ProductoDonado, pk=pk)

    if request.method == 'POST':
        # Si se envía un formulario POST de confirmación de eliminación
        producto_donado.delete()
        # Redirige a una URL después de la eliminación (puedes redirigir a donde necesites)
        return redirect('productos_donados')  # Cambia 'productos_donados' por la URL de la página de productos donados

    # Renderiza el template con el formulario de confirmación de eliminación
    return render(request, 'eliminar_producto_donado.html', {'producto_donado': producto_donado})


def eliminar_encuesta(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    
    if request.method == 'POST':
        encuesta.delete()
        return redirect('ver_encuestas')  # Cambia 'encuestas_list' por el nombre de la vista que muestra la lista de encuestas
    
    return render(request, 'eliminar_encuesta.html', {'encuesta': encuesta})