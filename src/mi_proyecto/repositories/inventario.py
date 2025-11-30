"""
Módulo de Repositorio - Inventario
Define las interfaces y servicios de acceso a datos
"""
from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from ..models.producto import Producto, Categoria

class RepositorioMemoria:
    """Almacena productos en memoria."""

    def __init__(self):
        self._productos: Dict[int, Producto] = {}

    def agregar(self, producto: Producto) -> bool:
        if producto.id_producto in self._productos:
            raise ValueError(f"El producto con ID {producto.id_producto} ya existe")
        self._productos[producto.id_producto] = producto
        return True

    def obtener(self, id_producto: int) -> Optional[Producto]:
        return self._productos.get(id_producto)

    def obtener_todos(self) -> List[Producto]:
        return list(self._productos.values())

    def eliminar(self, id_producto: int) -> bool:
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False
