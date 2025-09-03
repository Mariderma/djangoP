from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.productos.serializers import ProductoSerializer
from apps.productos.models import Producto

class ProductoListAPI(APIView):
	def get(self, request):
		productos = Producto.objects.all()
		serializer = ProductoSerializer(productos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ProductoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetailAPI(APIView):
	def get(self, request, pk):
		producto = Producto.objects(id=pk).first()
		if producto:
			serializer = ProductoSerializer(producto)
			return Response(serializer.data)
		return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, pk):
		producto = Producto.objects(id=pk).first()
		if not producto:
			return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
		serializer = ProductoSerializer(producto, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		producto = Producto.objects(id=pk).first()
		if not producto:
			return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
		producto.delete()
		return Response({'mensaje': 'Producto eliminado'}, status=status.HTTP_204_NO_CONTENT)