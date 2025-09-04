# Vista para actualizar producto
def admin_productos_update(request, pk):
    producto = Producto.objects(id=pk).first()
    if not producto:
        return redirect('admin-productos-list')
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.activo = bool(request.POST.get('activo'))
        producto.link_imagen = request.POST.get('link_imagen')
        producto.save()
        return redirect('admin-productos-list')
    return render(request, 'admin_productos_update.html', {'producto': producto})
from django.shortcuts import render, redirect
from apps.productos.models import Producto

# Vista para listar productos

def admin_productos_list(request):
    productos = Producto.objects.all()
    return render(request, 'admin_productos_list.html', {'productos': productos})

# Vista para crear producto

def admin_productos_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        activo = request.POST.get('activo', True)
        link_imagen = request.POST.get('link_imagen', '')
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            activo=activo,
            link_imagen=link_imagen
        )
        producto.save()
        return redirect('admin-productos-list')
    return render(request, 'admin_productos_create.html')

# Vista para eliminar producto

def admin_productos_delete(request, pk):
    producto = Producto.objects(id=pk).first()
    if producto:
        producto.delete()
    return redirect('admin-productos-list')
