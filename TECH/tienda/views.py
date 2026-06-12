"""
=====================================================
  TecnoStore UTC - Vistas (lógica de cada página)
=====================================================
Cada función aquí maneja una URL.
Recibe una petición (request) y devuelve una respuesta (HTML).
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .models import Producto, Categoria, MensajeBuzon, MensajeContacto, MensajeChat
from .forms import (
    FormularioRegistro, FormularioLogin, FormularioRecuperar,
    FormularioBuzon, FormularioContacto, FormularioBusqueda
)


# -------------------------------------------------------
# VISTA: Página de inicio
# -------------------------------------------------------
def inicio(request):
    """
    Muestra la página principal con productos destacados
    y categorías disponibles.
    """
    productos_destacados = Producto.objects.filter(destacado=True)[:6]
    categorias = Categoria.objects.all()
    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
        'titulo': 'Inicio',
    }
    return render(request, 'inicio.html', context)


# -------------------------------------------------------
# VISTA: Lista de productos
# -------------------------------------------------------
def productos(request):
    """
    Muestra todos los productos con opción de filtrar por categoría.
    """
    categoria_id = request.GET.get('categoria')
    todos_productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    categoria_activa = None

    if categoria_id:
        todos_productos = todos_productos.filter(categoria_id=categoria_id)
        try:
            categoria_activa = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            pass

    context = {
        'productos': todos_productos,
        'categorias': categorias,
        'categoria_activa': categoria_activa,
        'titulo': 'Productos',
    }
    return render(request, 'productos.html', context)


# -------------------------------------------------------
# VISTA: Detalle de producto
# -------------------------------------------------------
def detalle_producto(request, pk):
    """
    Muestra la información completa de un producto.
    Si el ID no existe, muestra error 404.
    """
    producto = get_object_or_404(Producto, pk=pk)
    # Productos relacionados de la misma categoría
    relacionados = Producto.objects.filter(
        categoria=producto.categoria
    ).exclude(pk=pk)[:4]

    context = {
        'producto': producto,
        'relacionados': relacionados,
        'titulo': producto.nombre,
    }
    return render(request, 'detalle_producto.html', context)


# -------------------------------------------------------
# VISTA: Ofertas
# -------------------------------------------------------
def ofertas(request):
    """
    Muestra solo los productos que están en oferta.
    """
    productos_oferta = Producto.objects.filter(es_oferta=True)
    context = {
        'productos': productos_oferta,
        'titulo': 'Ofertas',
    }
    return render(request, 'ofertas.html', context)


# -------------------------------------------------------
# VISTA: Registro de usuario
# -------------------------------------------------------
def registro(request):
    """
    Maneja el registro de nuevos usuarios.
    GET: muestra el formulario
    POST: procesa los datos y crea el usuario
    """
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            # Crear el usuario con los datos validados
            from django.contrib.auth.models import User
            user = User.objects.create_user(
                username=formulario.cleaned_data['username'],
                email=formulario.cleaned_data['email'],
                password=formulario.cleaned_data['password1'],
                first_name=formulario.cleaned_data['first_name'],
                last_name=formulario.cleaned_data['last_name'],
            )
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.first_name}! Tu cuenta fue creada exitosamente.')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        formulario = FormularioRegistro()

    return render(request, 'registro.html', {'formulario': formulario, 'titulo': 'Registro'})


# -------------------------------------------------------
# VISTA: Inicio de sesión
# -------------------------------------------------------
def iniciar_sesion(request):
    """
    Maneja el inicio de sesión de usuarios existentes.
    """
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        formulario = FormularioLogin(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            login(request, user)
            messages.success(request, f'¡Hola de nuevo, {user.first_name or user.username}!')
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        formulario = FormularioLogin()

    return render(request, 'login.html', {'formulario': formulario, 'titulo': 'Iniciar Sesión'})


# -------------------------------------------------------
# VISTA: Cerrar sesión
# -------------------------------------------------------
def cerrar_sesion(request):
    """
    Cierra la sesión del usuario y redirige al inicio.
    """
    logout(request)
    messages.info(request, 'Tu sesión fue cerrada correctamente.')
    return redirect('inicio')


# -------------------------------------------------------
# VISTA: Recuperar contraseña (simulada)
# -------------------------------------------------------
def recuperar(request):
    """
    Simula el proceso de recuperación de contraseña.
    En un proyecto real, enviaría un correo con un enlace.
    """
    enviado = False
    if request.method == 'POST':
        formulario = FormularioRecuperar(request.POST)
        if formulario.is_valid():
            enviado = True
            messages.success(
                request,
                'Si ese correo existe en nuestra base de datos, recibirás un enlace de recuperación (simulado).'
            )
    else:
        formulario = FormularioRecuperar()

    return render(request, 'recuperar.html', {
        'formulario': formulario,
        'enviado': enviado,
        'titulo': 'Recuperar Contraseña'
    })


# -------------------------------------------------------
# VISTA: Buzón de mensajes (requiere login)
# -------------------------------------------------------
@login_required
def buzon(request):
    """
    Muestra y gestiona el buzón de mensajes del usuario.
    @login_required: si no está logueado, redirige a /login/
    """
    if request.method == 'POST':
        formulario = FormularioBuzon(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)  # No guardar aún
            mensaje.usuario = request.user            # Asignar usuario
            mensaje.save()                            # Ahora sí guardar
            messages.success(request, '¡Mensaje enviado al buzón!')
            return redirect('buzon')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        formulario = FormularioBuzon()

    # Mostrar mensajes del usuario actual
    mis_mensajes = MensajeBuzon.objects.filter(usuario=request.user)

    return render(request, 'buzon.html', {
        'formulario': formulario,
        'mensajes': mis_mensajes,
        'titulo': 'Mi Buzón',
    })


# -------------------------------------------------------
# VISTA: Chat básico
# -------------------------------------------------------
def chat(request):
    """
    Chat básico de ayuda con respuestas automáticas.
    """
    # Usar session_key como ID de sesión del chat
    if not request.session.session_key:
        request.session.create()
    sesion_id = request.session.session_key

    historial = MensajeChat.objects.filter(sesion_id=sesion_id)

    return render(request, 'chat.html', {
        'historial': historial,
        'titulo': 'Chat de Ayuda',
    })


def chat_enviar(request):
    """
    Recibe el mensaje del usuario por AJAX y devuelve respuesta del bot.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('mensaje', '').strip()

        if not texto:
            return JsonResponse({'error': 'Mensaje vacío'}, status=400)

        if not request.session.session_key:
            request.session.create()
        sesion_id = request.session.session_key

        # Guardar mensaje del usuario
        MensajeChat.objects.create(
            sesion_id=sesion_id,
            tipo='usuario',
            mensaje=texto
        )

        # Generar respuesta automática del bot
        respuesta = generar_respuesta_bot(texto)

        # Guardar respuesta del bot
        MensajeChat.objects.create(
            sesion_id=sesion_id,
            tipo='bot',
            mensaje=respuesta
        )

        return JsonResponse({'respuesta': respuesta})

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def generar_respuesta_bot(texto):
    """
    Función simple que genera respuestas automáticas según palabras clave.
    """
    texto = texto.lower()

    if any(p in texto for p in ['hola', 'buenas', 'hey', 'hi']):
        return '¡Hola! Soy TecnoBot 🤖. ¿En qué te puedo ayudar hoy?'
    elif any(p in texto for p in ['precio', 'costo', 'cuánto', 'cuanto']):
        return '💰 Puedes ver todos los precios en nuestra sección de Productos. ¡También tenemos ofertas especiales!'
    elif any(p in texto for p in ['oferta', 'descuento', 'barato', 'promoción']):
        return '🏷️ ¡Tenemos excelentes ofertas! Visita la sección "Ofertas" en el menú para verlas todas.'
    elif any(p in texto for p in ['laptop', 'computadora', 'pc', 'notebook']):
        return '💻 Tenemos una gran selección de laptops. Ve a Productos > Laptops para explorarlas.'
    elif any(p in texto for p in ['celular', 'teléfono', 'smartphone', 'telefono']):
        return '📱 ¡Tenemos los mejores smartphones! Visita nuestra categoría de Celulares.'
    elif any(p in texto for p in ['envío', 'envio', 'entrega', 'shipping']):
        return '🚚 Realizamos envíos a toda la república. El tiempo estimado es de 3-5 días hábiles.'
    elif any(p in texto for p in ['pago', 'tarjeta', 'efectivo']):
        return '💳 Aceptamos tarjetas de crédito/débito, transferencias y efectivo en puntos de pago.'
    elif any(p in texto for p in ['ayuda', 'help', 'soporte', 'problema']):
        return '🆘 Puedes contactarnos en la sección "Contáctanos" o llamarnos al (844) 123-4567.'
    elif any(p in texto for p in ['gracias', 'thanks', 'ok', 'perfecto']):
        return '😊 ¡Con gusto! Si necesitas algo más, aquí estaré. ¡Que tengas un excelente día!'
    elif any(p in texto for p in ['adios', 'adiós', 'bye', 'hasta luego']):
        return '👋 ¡Hasta pronto! Gracias por visitar TecnoStore UTC.'
    else:
        return '🤔 No entendí bien tu pregunta. Puedes preguntarme sobre productos, precios, ofertas o envíos. ¡Estoy aquí para ayudar!'


# -------------------------------------------------------
# VISTA: Ayuda
# -------------------------------------------------------
def ayuda(request):
    """
    Página de preguntas frecuentes y ayuda.
    """
    faqs = [
        {
            'pregunta': '¿Cómo puedo registrarme?',
            'respuesta': 'Haz clic en "Registrar" en el menú de navegación, llena el formulario y listo.'
        },
        {
            'pregunta': '¿Los precios incluyen IVA?',
            'respuesta': 'Sí, todos los precios mostrados ya incluyen IVA.'
        },
        {
            'pregunta': '¿Cuánto tarda el envío?',
            'respuesta': 'Nuestros envíos tardan entre 3 y 5 días hábiles a toda la república.'
        },
        {
            'pregunta': '¿Puedo devolver un producto?',
            'respuesta': 'Sí, aceptamos devoluciones dentro de los primeros 30 días después de la compra.'
        },
        {
            'pregunta': '¿Cómo contacto al soporte?',
            'respuesta': 'Puedes usar el chat en línea, enviar mensaje al buzón o llenar el formulario de contacto.'
        },
        {
            'pregunta': '¿Tienen tienda física?',
            'respuesta': 'Sí, estamos en la Universidad Tecnológica de Coahuila (UTC), Saltillo, Coah.'
        },
    ]
    return render(request, 'ayuda.html', {'faqs': faqs, 'titulo': 'Ayuda'})


# -------------------------------------------------------
# VISTA: Contacto
# -------------------------------------------------------
def contacto(request):
    """
    Formulario de contacto para cualquier visitante.
    """
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Mensaje enviado! Te contactaremos pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        formulario = FormularioContacto()

    return render(request, 'contacto.html', {'formulario': formulario, 'titulo': 'Contáctanos'})


# -------------------------------------------------------
# VISTA: Mapa del sitio
# -------------------------------------------------------
def mapa_sitio(request):
    """
    Muestra todas las secciones y páginas del sitio.
    """
    secciones = {
        'principales': [
            {'nombre': 'Inicio', 'url': '/', 'icono': 'bi-house'},
            {'nombre': 'Productos', 'url': '/productos/', 'icono': 'bi-grid'},
            {'nombre': 'Ofertas', 'url': '/ofertas/', 'icono': 'bi-tag'},
        ],
        'secundarias': [
            {'nombre': 'Detalle de Producto', 'url': '/productos/', 'icono': 'bi-box'},
            {'nombre': 'Resultados de Búsqueda', 'url': '/buscar/', 'icono': 'bi-search'},
        ],
        'adicionales': [
            {'nombre': 'Registrarse', 'url': '/registro/', 'icono': 'bi-person-plus'},
            {'nombre': 'Iniciar Sesión', 'url': '/login/', 'icono': 'bi-box-arrow-in-right'},
            {'nombre': 'Cerrar Sesión', 'url': '/logout/', 'icono': 'bi-box-arrow-left'},
            {'nombre': 'Recuperar Contraseña', 'url': '/recuperar/', 'icono': 'bi-key'},
            {'nombre': 'Buzón', 'url': '/buzon/', 'icono': 'bi-envelope'},
            {'nombre': 'Chat de Ayuda', 'url': '/chat/', 'icono': 'bi-chat-dots'},
            {'nombre': 'Ayuda / FAQ', 'url': '/ayuda/', 'icono': 'bi-question-circle'},
            {'nombre': 'Contáctanos', 'url': '/contacto/', 'icono': 'bi-telephone'},
            {'nombre': 'Mapa del Sitio', 'url': '/mapa-sitio/', 'icono': 'bi-map'},
            {'nombre': 'Página de Error 404', 'url': '/404/', 'icono': 'bi-exclamation-triangle'},
        ],
    }
    return render(request, 'mapa_sitio.html', {'secciones': secciones, 'titulo': 'Mapa del Sitio'})


# -------------------------------------------------------
# VISTA: Búsqueda
# -------------------------------------------------------
def buscar(request):
    """
    Busca productos por nombre o categoría.
    """
    formulario = FormularioBusqueda(request.GET)
    resultados = []
    query = ''

    if formulario.is_valid():
        query = formulario.cleaned_data.get('q', '')
        if query:
            resultados = Producto.objects.filter(
                nombre__icontains=query
            ) | Producto.objects.filter(
                categoria__nombre__icontains=query
            ) | Producto.objects.filter(
                descripcion__icontains=query
            )
            resultados = resultados.distinct()

    return render(request, 'buscar.html', {
        'formulario': formulario,
        'resultados': resultados,
        'query': query,
        'titulo': f'Búsqueda: {query}' if query else 'Buscar',
    })


# -------------------------------------------------------
# VISTA: Error 404 personalizado
# -------------------------------------------------------
def error_404(request, exception):
    """
    Página de error 404 personalizada y bonita.
    Se activa cuando alguien entra a una URL que no existe.
    """
    return render(request, '404.html', {'titulo': 'Página no encontrada'}, status=404)


# -------------------------------------------------------
# VISTA: Demo de página 404 (accesible siempre, con diseño)
# -------------------------------------------------------
def demo_404(request):
    """
    Muestra la página 404 personalizada con todo el diseño.
    Accesible desde /404/ sin necesitar DEBUG=False.
    """
    return render(request, '404.html', {'titulo': 'Página no encontrada'})
