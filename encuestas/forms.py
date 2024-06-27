from django import forms
from .models import Encuesta, ResultadoEncuesta, ProductoDonado

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['texto_encuesta', 'activa']

class ResultadoEncuestaForm(forms.ModelForm):
    class Meta:
        model = ResultadoEncuesta
        fields = ['respuesta']
        widgets = {
            'respuesta': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 8)])
        }

class ProductoDonadoForm(forms.ModelForm):
    class Meta:
        model = ProductoDonado
        fields = ['nombre', 'imagen', 'calificacion']