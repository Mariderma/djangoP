from mongoengine import Document, StringField, DecimalField, IntField, BooleanField, URLField

class Producto(Document):
    nombre = StringField(max_length=100, required=True)
    descripcion = StringField()
    precio = DecimalField(precision=2, required=True)
    stock = IntField(required=True)
    activo = BooleanField(default=True)
    link_imagen = URLField(required=False)

    def __str__(self):
        return self.nombre
    
from apps.productos.models import Producto

# Crear un producto
nuevo_producto = Producto(
    nombre="Ejemplo",
    descripcion="Descripción de ejemplo",
    precio=99.99,
    stock=10,
    activo=True,
    link_imagen="https://ejemplo.com/imagen.jpg"
)
nuevo_producto.save()

# Consultar todos los productos
productos = Producto.objects.all()
for producto in productos:
    print(producto.nombre, producto.precio)

# Buscar por nombre
producto = Producto.objects(nombre="Ejemplo").first()
print(producto.descripcion)