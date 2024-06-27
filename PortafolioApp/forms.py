# PortafolioApp/forms.py

from django import forms
from .models import Noticia, Categoria

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'imagen', 'categoria']  # Ajusta los campos según tu modelo Noticia
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),
            'categoria': forms.Select(choices=Categoria.objects.all())
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']