"""
=====================================================
  TecnoStore UTC - Formularios con validación
=====================================================
Los formularios en Django validan datos del lado
del servidor (backend). Siempre validamos aquí
además de en el HTML (frontend).
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import MensajeBuzon, MensajeContacto


# -------------------------------------------------------
# FORMULARIO: Registro de usuario
# -------------------------------------------------------
class FormularioRegistro(forms.Form):
    """
    Formulario para que nuevos usuarios se registren.
    Incluye validación anti-bots con pregunta matemática.
    """
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: yahir_tec',
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
        })
    )
    first_name = forms.CharField(
        label="Nombre(s)",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre',
        })
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tus apellidos',
        })
    )
    password1 = forms.CharField(
        label="Contraseña",
        min_length=6,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mínimo 6 caracteres',
        })
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repite tu contraseña',
        })
    )
    # --- Validación anti-bots (pregunta humana) ---
    captcha_respuesta = forms.IntegerField(
        label="¿Cuánto es 3 + 4? (verificación humana)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe el resultado',
        })
    )

    # --- Validaciones personalizadas (backend) ---

    def clean_username(self):
        """Verifica que el nombre de usuario no esté ocupado."""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ese nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        """Verifica que el correo no esté registrado."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con ese correo.")
        return email

    def clean_password2(self):
        """Verifica que las dos contraseñas coincidan."""
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return p2

    def clean_captcha_respuesta(self):
        """Verifica la respuesta del captcha matemático."""
        respuesta = self.cleaned_data.get('captcha_respuesta')
        if respuesta != 7:  # 3 + 4 = 7
            raise forms.ValidationError("Respuesta incorrecta. ¿Cuánto es 3 + 4?")
        return respuesta


# -------------------------------------------------------
# FORMULARIO: Inicio de sesión
# -------------------------------------------------------
class FormularioLogin(AuthenticationForm):
    """
    Extiende el formulario de login de Django
    para añadir estilos Bootstrap.
    """
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre de usuario',
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu contraseña',
        })
    )


# -------------------------------------------------------
# FORMULARIO: Recuperar contraseña (simulado)
# -------------------------------------------------------
class FormularioRecuperar(forms.Form):
    """
    Formulario de recuperación de contraseña.
    En este proyecto es simulado (no envía correo real).
    """
    email = forms.EmailField(
        label="Correo electrónico registrado",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No encontramos una cuenta con ese correo.")
        return email


# -------------------------------------------------------
# FORMULARIO: Buzón de mensajes
# -------------------------------------------------------
class FormularioBuzon(forms.ModelForm):
    """
    Formulario para enviar mensajes al buzón.
    Usa ModelForm para ligarse directo al modelo MensajeBuzon.
    """
    class Meta:
        model = MensajeBuzon
        fields = ['asunto', 'mensaje']
        widgets = {
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto de tu mensaje',
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribe tu mensaje aquí...',
            }),
        }
        labels = {
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }


# -------------------------------------------------------
# FORMULARIO: Contacto
# -------------------------------------------------------
class FormularioContacto(forms.ModelForm):
    """
    Formulario de contacto público (sin necesidad de login).
    """
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@correo.com',
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Motivo de contacto',
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribe tu mensaje...',
            }),
        }
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }


# -------------------------------------------------------
# FORMULARIO: Búsqueda
# -------------------------------------------------------
class FormularioBusqueda(forms.Form):
    """
    Formulario simple para buscar productos.
    """
    q = forms.CharField(
        label="Buscar",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar productos...',
        })
    )
