from django.urls import path
from apps.productos.views import ProductoListAPI, ProductoDetailAPI
from apps.productos import admin_views

urlpatterns = [
    path('productos/', ProductoListAPI.as_view(), name='producto-list'),
    path('productos/<str:pk>/', ProductoDetailAPI.as_view(), name='producto-detail'),
    path('admin/productos/', admin_views.admin_productos_list, name='admin-productos-list'),
    path('admin/productos/crear/', admin_views.admin_productos_create, name='admin-productos-create'),
    path('admin/productos/eliminar/<str:pk>/', admin_views.admin_productos_delete, name='admin-productos-delete'),
    path('admin/productos/editar/<str:pk>/', admin_views.admin_productos_update, name='admin-productos-update'),
]