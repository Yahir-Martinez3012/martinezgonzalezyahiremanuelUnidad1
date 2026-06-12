# TecnoStore UTC — Guía de instalación para Yahir
## Proyecto: MartinezGonzalezYahirEmanuelUnidad1

---

## REQUISITOS PREVIOS

Antes de empezar, necesitas tener instalado en tu computadora:

1. **Python 3.10 o superior**
   - Descárgalo de: https://www.python.org/downloads/
   - IMPORTANTE: Al instalar, marca la casilla **"Add Python to PATH"**

2. **Visual Studio Code**
   - Descárgalo de: https://code.visualstudio.com/
   - Instala la extensión **"Python"** de Microsoft (busca en Extensions)

3. **Git** (para subir a GitHub después)
   - Descárgalo de: https://git-scm.com/

---

## PASO 1 — Colocar el proyecto

1. Copia la carpeta `MartinezGonzalezYahirEmanuelUnidad1` a tu escritorio
   (o a donde quieras, por ejemplo: `C:\Proyectos\`)

2. Abre **Visual Studio Code**

3. Ve a `File → Open Folder` y selecciona la carpeta del proyecto

---

## PASO 2 — Abrir la terminal en VS Code

En VS Code presiona: **Ctrl + ` ** (tecla de acento grave, arriba del Tab)

Esto abre la terminal integrada de VS Code.

---

## PASO 3 — Crear el entorno virtual

Un entorno virtual es como una "cajita" donde instalamos Django sin afectar
el resto de tu computadora.

Escribe esto en la terminal (una línea a la vez):

```
python -m venv venv
```

Luego actívalo:

```
venv\Scripts\activate
```

 Sabrás que está activado cuando aparezca `(venv)` al inicio de la línea.

---

## PASO 4 — Instalar Django

Con el entorno virtual activo, escribe:

```
pip install django
```

Espera a que termine (puede tardar 1-2 minutos).

Para verificar que se instaló correctamente:

```
python -m django --version
```

Deberías ver algo como: `5.x.x`

---

## PASO 5 — Crear las tablas de la base de datos

Django necesita crear las tablas en la base de datos SQLite.
Escribe estos dos comandos:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Verás varios mensajes con "OK" — eso es normal y bueno.

---

## PASO 6 — Crear el superusuario (admin)

Este usuario te permitirá entrar al panel de administración
en `/admin/` para agregar productos.

```
python manage.py createsuperuser
```

Te pedirá:
- **Username**: pon algo como `admin` o `yahir`
- **Email**: tu correo (o déjalo vacío y presiona Enter)
- **Password**: una contraseña (mínimo 8 caracteres)
  ⚠️ Al escribir la contraseña NO se ven los caracteres — eso es normal

---

## PASO 7 — Cargar productos de ejemplo

Para que la tienda se vea llena con productos desde el inicio:

```
python poblar_datos.py
```

Verás mensajes ✅ para cada categoría y producto creado.

---

## PASO 8 — ¡Encender el servidor!

```
python manage.py runserver
```

Verás algo como:
```
Starting development server at http://127.0.0.1:8000/
```

Ahora abre tu navegador y entra a: **http://127.0.0.1:8000/**

---

## PÁGINAS DEL SITIO

| Página | URL |
|--------|-----|
| Inicio | http://127.0.0.1:8000/ |
| Productos | http://127.0.0.1:8000/productos/ |
| Ofertas | http://127.0.0.1:8000/ofertas/ |
| Registro | http://127.0.0.1:8000/registro/ |
| Login | http://127.0.0.1:8000/login/ |
| Buzón | http://127.0.0.1:8000/buzon/ |
| Chat | http://127.0.0.1:8000/chat/ |
| Ayuda | http://127.0.0.1:8000/ayuda/ |
| Contacto | http://127.0.0.1:8000/contacto/ |
| Mapa del sitio | http://127.0.0.1:8000/mapa-sitio/ |
| Búsqueda | http://127.0.0.1:8000/buscar/ |
| Panel Admin | http://127.0.0.1:8000/admin/ |
| Error 404 | http://127.0.0.1:8000/pagina-inventada/ |

---

## Para detener el servidor

En la terminal presiona: **Ctrl + C**

---

## La próxima vez que quieras correrlo

Solo necesitas hacer el PASO 3 (activar venv) y PASO 8 (runserver):

```
venv\Scripts\activate
python manage.py runserver
```

---

## CAPTURAS QUE NECESITAS PARA EL PDF

Toma capturas de pantalla de estas páginas:

1. ✅ **Inicio** — http://127.0.0.1:8000/
2. ✅ **Menú de navegación** — Despliega el menú "⋮"
3. ✅ **Productos** — http://127.0.0.1:8000/productos/
4. ✅ **Detalle de producto** — Clic en cualquier producto
5. ✅ **Ofertas** — http://127.0.0.1:8000/ofertas/
6. ✅ **Búsqueda** — Busca "laptop" en el buscador
7. ✅ **Registro con validación** — http://127.0.0.1:8000/registro/ (intenta enviar vacío)
8. ✅ **Login** — http://127.0.0.1:8000/login/
9. ✅ **Recuperar contraseña** — http://127.0.0.1:8000/recuperar/
10. ✅ **Buzón** — http://127.0.0.1:8000/buzon/ (después de hacer login)
11. ✅ **Chat** — http://127.0.0.1:8000/chat/ (escribe "hola")
12. ✅ **Contacto** — http://127.0.0.1:8000/contacto/
13. ✅ **Mapa del sitio** — http://127.0.0.1:8000/mapa-sitio/
14. ✅ **Error 404** — http://127.0.0.1:8000/cualquier-cosa-inventada/
15. ✅ **Panel admin** — http://127.0.0.1:8000/admin/

---

## SOLUCIÓN DE PROBLEMAS

**"python no se reconoce como comando"**
→ Reinstala Python marcando "Add Python to PATH"

**"No module named django"**
→ Asegúrate de tener el entorno virtual activo: `venv\Scripts\activate`

**La página dice "DEBUG=False"**
→ Abre `tecnostore_utc/settings.py` y asegúrate que `DEBUG = True`

**Error al hacer makemigrations**
→ Asegúrate de estar en la carpeta correcta (donde está `manage.py`)

---

##  SUBIR A GITHUB

```
git init
git add .
git commit -m "Proyecto TecnoStore UTC - Unidad 1"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/MartinezGonzalezYahirEmanuelUnidad1.git
git push -u origin main
```

---

*Desarrollado por: Martinez González Yahir Emanuel*
*Materia: Desarrollo Web con Python*
*Universidad Tecnológica de Coahuila (UTC)*
