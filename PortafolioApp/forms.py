# PortafolioApp/forms.py

from django import forms
from .models import Noticia,Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'imagen']  # Ajusta los campos según tu modelo Noticia
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),
        }

