"""
TecnoStore UTC - Datos de ejemplo
Imagenes desde placehold.co (siempre disponibles, sin bloqueos)
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecnostore_utc.settings')
django.setup()

from tienda.models import Categoria, Producto

Producto.objects.all().delete()
Categoria.objects.all().delete()
print("Datos anteriores eliminados.")

cats = {}
for c in [
    {'nombre': 'Laptops',    'icono': 'bi-laptop',     'descripcion': 'Computadoras portátiles'},
    {'nombre': 'Celulares',  'icono': 'bi-phone',      'descripcion': 'Smartphones y teléfonos'},
    {'nombre': 'Audifonos',  'icono': 'bi-headphones', 'descripcion': 'Audio y sonido'},
    {'nombre': 'Accesorios', 'icono': 'bi-mouse',      'descripcion': 'Mouse, teclados y más'},
    {'nombre': 'Tablets',    'icono': 'bi-tablet',     'descripcion': 'Tabletas digitales'},
    {'nombre': 'Monitores',  'icono': 'bi-display',    'descripcion': 'Pantallas y monitores'},
]:
    cats[c['nombre']] = Categoria.objects.create(**c)
    print(f"  Categoria: {c['nombre']}")

# Imagenes tecnologicas reales que cargan sin restricciones
# Fuente: unsplash.com con parametros especificos que si permiten hotlinking
productos = [
    # LAPTOPS
    {
        'nombre': 'Laptop HP Pavilion 15 Core i5',
        'descripcion': 'Intel Core i5-1135G7, 8GB RAM DDR4, SSD 256GB, pantalla Full HD 15.6 pulgadas, Windows 11 Home. Bateria hasta 9 horas. Color plata.',
        'precio': 13999.00, 'precio_oferta': 11499.00,
        'categoria': 'Laptops',
        'imagen_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&q=80',
        'stock': 12, 'es_oferta': True, 'destacado': True,
    },
    {
        'nombre': 'MacBook Air M2 13 pulgadas',
        'descripcion': 'Chip Apple M2 de 8 nucleos, 8GB RAM unificada, SSD 256GB, pantalla Liquid Retina 13.6 pulgadas, hasta 18 horas de bateria. Ultradelgado.',
        'precio': 28999.00, 'precio_oferta': None,
        'categoria': 'Laptops',
        'imagen_url': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&q=80',
        'stock': 6, 'es_oferta': False, 'destacado': True,
    },
    {
        'nombre': 'Lenovo IdeaPad 3 AMD Ryzen 5',
        'descripcion': 'AMD Ryzen 5 5500U, 8GB RAM, 512GB SSD, Full HD 15.6 pulgadas, Windows 11. Excelente para programacion y trabajo universitario.',
        'precio': 10999.00, 'precio_oferta': 9299.00,
        'categoria': 'Laptops',
        'imagen_url': 'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&q=80',
        'stock': 18, 'es_oferta': True, 'destacado': False,
    },
    {
        'nombre': 'Dell Inspiron 15 Core i7',
        'descripcion': 'Intel Core i7-1165G7, 16GB RAM, SSD 512GB, NVIDIA MX350, pantalla FHD 15.6 pulgadas. Ideal para ingenieria y diseno grafico.',
        'precio': 19499.00, 'precio_oferta': 16999.00,
        'categoria': 'Laptops',
        'imagen_url': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&q=80',
        'stock': 8, 'es_oferta': True, 'destacado': True,
    },
    # CELULARES
    {
        'nombre': 'Samsung Galaxy A54 5G 128GB',
        'descripcion': 'Super AMOLED 6.4 pulgadas FHD+, Exynos 1380, 8GB RAM, camara triple 50+12+5 MP, bateria 5000 mAh, carga rapida 25W. Color negro.',
        'precio': 9499.00, 'precio_oferta': 7999.00,
        'categoria': 'Celulares',
        'imagen_url': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&q=80',
        'stock': 25, 'es_oferta': True, 'destacado': True,
    },
    {
        'nombre': 'iPhone 15 128GB Negro',
        'descripcion': 'Chip A16 Bionic, camara 48MP con zoom optico 2x, Dynamic Island, USB-C, pantalla Super Retina XDR 6.1 pulgadas, iOS 17.',
        'precio': 19999.00, 'precio_oferta': None,
        'categoria': 'Celulares',
        'imagen_url': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600&q=80',
        'stock': 10, 'es_oferta': False, 'destacado': True,
    },
    {
        'nombre': 'Xiaomi Redmi Note 13 Pro 256GB',
        'descripcion': 'AMOLED 6.67 pulgadas 120Hz, Snapdragon 7s Gen 2, 8GB RAM, camara 200MP, bateria 5000 mAh con carga turbo 67W.',
        'precio': 7499.00, 'precio_oferta': 5999.00,
        'categoria': 'Celulares',
        'imagen_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&q=80',
        'stock': 30, 'es_oferta': True, 'destacado': False,
    },
    # AUDIFONOS
    {
        'nombre': 'Sony WH-1000XM5 Negros',
        'descripcion': 'Cancelacion de ruido activa, audio Hi-Res, 30 horas de bateria, carga rapida 3 min para 3 horas. Los mejores audifonos del mercado.',
        'precio': 8999.00, 'precio_oferta': 6999.00,
        'categoria': 'Audifonos',
        'imagen_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80',
        'stock': 15, 'es_oferta': True, 'destacado': True,
    },
    {
        'nombre': 'AirPods Pro 2da Generacion',
        'descripcion': 'Chip H2, cancelacion activa de ruido mejorada, audio espacial personalizado, hasta 30 horas con estuche MagSafe, resistencia al agua IPX4.',
        'precio': 6499.00, 'precio_oferta': None,
        'categoria': 'Audifonos',
        'imagen_url': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=600&q=80',
        'stock': 12, 'es_oferta': False, 'destacado': False,
    },
    {
        'nombre': 'JBL Tune 510BT Azul',
        'descripcion': 'On-ear Bluetooth, sonido Pure Bass JBL, 40 horas de bateria, plegables, carga rapida 5 min para 2 horas.',
        'precio': 1299.00, 'precio_oferta': 999.00,
        'categoria': 'Audifonos',
        'imagen_url': 'https://images.unsplash.com/photo-1546435770-a3e736ce0e31?w=600&q=80',
        'stock': 35, 'es_oferta': True, 'destacado': False,
    },
    # ACCESORIOS
    {
        'nombre': 'Mouse Logitech MX Master 3S',
        'descripcion': 'Sensor 8000 DPI, scroll MagSpeed, 7 botones programables, USB-C y Bluetooth. Compatible con Windows y Mac. Color grafito.',
        'precio': 2199.00, 'precio_oferta': 1799.00,
        'categoria': 'Accesorios',
        'imagen_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&q=80',
        'stock': 28, 'es_oferta': True, 'destacado': False,
    },
    {
        'nombre': 'Teclado Mecanico Redragon K552 RGB',
        'descripcion': 'TKL 87 teclas, switches Outemu Blue, retroiluminacion RGB, estructura metalica, anti-ghosting completo. Ideal para programar.',
        'precio': 699.00, 'precio_oferta': 549.00,
        'categoria': 'Accesorios',
        'imagen_url': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=600&q=80',
        'stock': 40, 'es_oferta': True, 'destacado': True,
    },
    # TABLETS
    {
        'nombre': 'iPad 10ma Generacion 64GB WiFi',
        'descripcion': 'Chip A14 Bionic, pantalla Liquid Retina 10.9 pulgadas, camara delantera 12MP, USB-C, WiFi 6, hasta 10 horas de bateria.',
        'precio': 10999.00, 'precio_oferta': 9499.00,
        'categoria': 'Tablets',
        'imagen_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&q=80',
        'stock': 14, 'es_oferta': True, 'destacado': True,
    },
    {
        'nombre': 'Samsung Galaxy Tab A8 128GB',
        'descripcion': 'Pantalla 10.5 pulgadas TFT, 4GB RAM, bateria 7040 mAh, Android 13, Four Speakers Dolby Atmos. Ideal para ver clases y estudiar.',
        'precio': 5999.00, 'precio_oferta': 4799.00,
        'categoria': 'Tablets',
        'imagen_url': 'https://images.unsplash.com/photo-1632160606765-cc5e4ec5dfbe?w=600&q=80',
        'stock': 18, 'es_oferta': True, 'destacado': False,
    },
    # MONITORES
    {
        'nombre': 'Monitor LG 24 pulgadas Full HD IPS',
        'descripcion': 'Panel IPS 24 pulgadas 1920x1080, 75Hz, 5ms, AMD FreeSync, entradas HDMI y VGA. Perfecto para trabajo y estudio en casa.',
        'precio': 3299.00, 'precio_oferta': 2799.00,
        'categoria': 'Monitores',
        'imagen_url': 'https://images.unsplash.com/photo-1547082299-de196ea013d6?w=600&q=80',
        'stock': 16, 'es_oferta': True, 'destacado': False,
    },
    {
        'nombre': 'Monitor Samsung 27 pulgadas Curvo 144Hz',
        'descripcion': 'Panel VA curvo 1500R, QHD 2560x1440, 144Hz, 1ms MPRT, AMD FreeSync Premium, HDR10. Gaming y trabajo profesional.',
        'precio': 6999.00, 'precio_oferta': 5799.00,
        'categoria': 'Monitores',
        'imagen_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=600&q=80',
        'stock': 9, 'es_oferta': True, 'destacado': True,
    },
]

for p in productos:
    cat_nombre = p.pop('categoria')
    p['categoria'] = cats[cat_nombre]
    prod = Producto.objects.create(**p)
    oferta = f" -> ${prod.precio_oferta:,.0f}" if prod.precio_oferta else ""
    print(f"  Producto: {prod.nombre[:50]:<50} ${prod.precio:>9,.0f} MXN{oferta}")

print(f"\nListo:")
print(f"  {Producto.objects.count()} productos")
print(f"  {Categoria.objects.count()} categorias")
print(f"  {Producto.objects.filter(es_oferta=True).count()} en oferta")
print(f"  {Producto.objects.filter(destacado=True).count()} destacados")
print(f"\npython manage.py runserver -> http://127.0.0.1:8000/")
