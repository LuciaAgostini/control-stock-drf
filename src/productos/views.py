from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto, Proveedor
from .serializers import ProductoSerializer, ProveedorSerializer


# CRUD DE PROVEEDORES

class ProveedorListCreateView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProveedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


# CRUD DE PRODUCTOS

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.select_related("proveedor").all()
    serializer_class = ProductoSerializer


class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.select_related("proveedor").all()
    serializer_class = ProductoSerializer


# AJUSTAR STOCK DE UN PRODUCTO

class ProductoAjustarStockView(APIView):

    def post(self, request, pk):

        cantidad = request.data.get("cantidad")

        if cantidad is None:
            return Response(
                {"detail": "Debés enviar el campo 'cantidad'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if isinstance(cantidad, bool):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if str(cantidad) != str(request.data.get("cantidad")):
            return Response(
                {"detail": "La cantidad debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            producto = get_object_or_404(
                Producto.objects.select_for_update(),
                pk=pk
            )

            nuevo_stock = producto.cantidad_stock + cantidad

            if nuevo_stock < 0:
                return Response(
                    {"detail": "No hay stock suficiente para esa salida."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            producto.cantidad_stock = nuevo_stock
            producto.save()

        serializer = ProductoSerializer(producto)

        return Response(serializer.data)