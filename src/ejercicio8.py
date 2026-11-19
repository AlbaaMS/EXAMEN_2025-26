from collections import namedtuple

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_compra'  # tipo date
])

def categoria_mayor_gasto(productos: list[Producto]) -> tuple[str, float] | None:
    """
    Determina la categoría con el mayor gasto total. Devuelve el nombre de la categoría
    junto con el gasto total en esa categoría.

    Si la lista de productos está vacía, devuelve None.

    Parámetros:
    productos (list[Producto]): Lista de productos.

    Devuelve:
    tuple[str, float] | None: La categoría con el mayor gasto total y el gasto total, o None si la lista de productos está vacía.
    """
    gastos = {}
    max = tuple()
    if not productos:
        return None
    for prod in productos: #buscamos en la lista productos
        if prod.categoria in gastos:
            gastos[prod.categoria] += prod.precio
        else:
            gastos[prod.categoria] = prod.precio

    for categ, precio in gastos.items(): #miramos en los objetos del diccionario gastos
        if not max:
            max = (categ,precio)
        if precio > max[1]:
            max = (categ,precio)
    return max
        
    