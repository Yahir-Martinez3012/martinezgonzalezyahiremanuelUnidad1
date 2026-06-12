"""
=====================================================
  TecnoStore UTC - Modelos de base de datos
=====================================================
Los modelos son clases que representan tablas en la BD.
Cada atributo de la clase = una columna en la tabla.
"""

from django.db import models
from django.contrib.auth.models import User


# -------------------------------------------------------
# MODELO: Categoría de producto
# -------------------------------------------------------
class Categoria(models.Model):
    """
    Representa una categoría de productos.
    Ejemplo: Laptops, Celulares, Accesorios
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    icono = models.CharField(
        max_length=50, default='bi-box',
        verbose_name="Ícono Bootstrap",
        help_text="Ejemplo: bi-laptop, bi-phone, bi-headphones"
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# -------------------------------------------------------
# MODELO: Producto
# -------------------------------------------------------
class Producto(models.Model):
    """
    Representa un producto tecnológico en la tienda.
    """
    nombre = models.CharField(max_length=200, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ($)")
    precio_oferta = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        verbose_name="Precio en oferta ($)"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE,
        verbose_name="Categoría",
        related_name='productos'
    )
    imagen_url = models.URLField(
        blank=True,
        verbose_name="URL de imagen",
        help_text="Pega aquí la URL de una imagen del producto"
    )
    stock = models.PositiveIntegerField(default=1, verbose_name="Unidades disponibles")
    es_oferta = models.BooleanField(default=False, verbose_name="¿Está en oferta?")
    destacado = models.BooleanField(default=False, verbose_name="¿Producto destacado?")
    fecha_agregado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_agregado']

    def __str__(self):
        return self.nombre

    def tiene_oferta(self):
        """Retorna True si el producto tiene precio de oferta."""
        return self.precio_oferta is not None and self.precio_oferta < self.precio

    def porcentaje_descuento(self):
        """Calcula el % de descuento si hay oferta."""
        if self.tiene_oferta():
            descuento = ((self.precio - self.precio_oferta) / self.precio) * 100
            return int(descuento)
        return 0


# -------------------------------------------------------
# MODELO: Mensaje del buzón
# -------------------------------------------------------
class MensajeBuzon(models.Model):
    """
    Guarda los mensajes que los usuarios envían al buzón.
    """
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Usuario",
        related_name='mensajes_buzon'
    )
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")
    leido = models.BooleanField(default=False, verbose_name="¿Leído?")

    class Meta:
        verbose_name = "Mensaje de Buzón"
        verbose_name_plural = "Mensajes de Buzón"
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"{self.usuario.username} - {self.asunto}"


# -------------------------------------------------------
# MODELO: Mensaje de contacto
# -------------------------------------------------------
class MensajeContacto(models.Model):
    """
    Guarda los mensajes del formulario de contacto.
    Cualquier visitante puede enviar uno (no requiere login).
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo electrónico")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"


# -------------------------------------------------------
# MODELO: Mensaje de Chat
# -------------------------------------------------------
class MensajeChat(models.Model):
    """
    Guarda el historial del chat básico de ayuda.
    """
    TIPO_CHOICES = [
        ('usuario', 'Usuario'),
        ('bot', 'Bot'),
    ]
    sesion_id = models.CharField(max_length=100, verbose_name="ID de sesión")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name="Tipo")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        verbose_name = "Mensaje de Chat"
        verbose_name_plural = "Mensajes de Chat"
        ordering = ['fecha']

    def __str__(self):
        return f"[{self.tipo}] {self.mensaje[:50]}"
