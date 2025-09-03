from django.urls import path
from apps.productos.views import ProductoListAPI, ProductoDetailAPI

urlpatterns = [
    path('productos/', ProductoListAPI.as_view(), name='producto-list'),
    path('productos/<str:pk>/', ProductoDetailAPI.as_view(), name='producto-detail'),
]