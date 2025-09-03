from rest_framework import serializers
from apps.productos.models import Producto

class ProductoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    descripcion = serializers.CharField()
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    activo = serializers.BooleanField(default=True)
    link_imagen = serializers.URLField(allow_blank=True)

    def to_representation(self, instance):
        # MongoEngine usa .id como ObjectId
        return {
            'id': str(instance.id),
            'nombre': instance.nombre,
            'descripcion': instance.descripcion,
            'precio': float(instance.precio),
            'stock': instance.stock,
            'activo': instance.activo,
            'link_imagen': instance.link_imagen
        }

    def create(self, validated_data):
        return Producto(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance