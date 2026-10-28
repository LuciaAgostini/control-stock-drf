# API de Control de Stock — Primer Práctico DRF

Proyecto para el Primer Práctico de "Ingeniería de Software" (ITEC).
Temática elegida: **control de stock de productos**.

## Contenido

- Modelo `Producto` (nombre, SKU, categoría, precio, cantidad en stock, stock mínimo, activo)
- Serializer `ProductoSerializer` (ModelSerializer, incluye `stock_bajo` calculado)
- Vistas funcionales de CRUD con `@api_view`:
  - `GET   /api/productos/`                     -> listar productos
  - `POST  /api/productos/`                     -> dar de alta un producto
  - `GET   /api/productos/<id>/`                -> ver detalle
  - `PUT   /api/productos/<id>/`                -> actualizar completo
  - `PATCH /api/productos/<id>/`                -> actualizar parcial
  - `DELETE /api/productos/<id>/`               -> eliminar producto
  - `POST  /api/productos/<id>/ajustar-stock/`  -> extra: sumar/restar unidades de stock

## Cómo correr el proyecto

### 1. Instalar dependencias con uv

```
uv sync
```

### 2. Entrar en src y migrar

```
cd src
uv run manage.py migrate
```

### 3. (Opcional) Crear superusuario para el admin

```
uv run manage.py createsuperuser
```

### 4. Levantar el servidor

```
uv run manage.py runserver
```

La API queda disponible en:

```
http://127.0.0.1:8000/api/productos/
```

El panel de administración en:

```
http://127.0.0.1:8000/admin/
```

## Ejemplo de body para crear un producto (POST)

```json
{
  "nombre": "Mouse inalámbrico",
  "sku": "MOU-001",
  "categoria": "Periféricos",
  "precio": "8500.00",
  "cantidad_stock": 30,
  "stock_minimo": 5
}
```

## Ejemplo de body para ajustar stock (POST a /ajustar-stock/)

```json
{ "cantidad": -3 }
```

Resta 3 unidades del stock actual (por ejemplo, tras una venta).
Usá un número positivo para sumar unidades (por ejemplo, tras una compra).

## Probar los endpoints

Se recomienda usar Postman, Bruno o ThunderClient para probar los endpoints.
