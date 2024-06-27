from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordResetForm,
                                       SetPasswordForm
                                       )
from .models import Profile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Nombre de Usuario"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Contraseña"
    }))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Correo"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'contraseña'
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'confirma contraseña'
    }))


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('natural', 'Persona Natural'),
        ('company', 'Empresa'),
        ('admin', 'Administrador'),
    ]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Nombre de Usuario"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Correo"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Contraseña"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Confirma contraseña"
    }))
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.Select(attrs={
        "class": "input",
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
            profile.save()
        return user