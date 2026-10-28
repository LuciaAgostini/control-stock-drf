from django.urls import path

from .views import (
    ProductoListCreateView,
    ProductoDetailView,
    ProductoAjustarStockView,
    ProveedorListCreateView,
    ProveedorDetailView,
)

urlpatterns = [

    # Rutas de productos

    path(
        "productos/",
        ProductoListCreateView.as_view(),
        name="producto-list"
    ),

    path(
        "productos/<int:pk>/",
        ProductoDetailView.as_view(),
        name="producto-detail"
    ),

    path(
        "productos/<int:pk>/ajustar-stock/",
        ProductoAjustarStockView.as_view(),
        name="producto-ajustar-stock"
    ),

    # Rutas de proveedores

    path(
        "proveedores/",
        ProveedorListCreateView.as_view(),
        name="proveedor-list"
    ),

    path(
        "proveedores/<int:pk>/",
        ProveedorDetailView.as_view(),
        name="proveedor-detail"
    ),

]