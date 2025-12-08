"""
Paquete repositories - Capa de Acceso a Datos
==============================================

Este paquete contiene las clases responsables de la persistencia y 
gestión de datos del sistema. Implementa el patrón Repository para
separar la lógica de negocio del almacenamiento de datos.

Módulos:
--------
- inventario.py: Contiene RepositorioMemoria e Inventario.
                 - RepositorioMemoria: Almacena productos en memoria (diccionario)
                 - Inventario: Gestiona las operaciones del inventario (CRUD y lógica)

Clases principales:
-------------------
- RepositorioMemoria: Almacenamiento en memoria de productos
- Inventario: Gestión de operaciones sobre el inventario (agregar, aumentar/disminuir stock)

Ejemplo de uso:
---------------
>>> from repositories.inventario import RepositorioMemoria, Inventario
>>> repo = RepositorioMemoria()
>>> inventario = Inventario(repo)
>>> inventario.agregar_producto("Martillo", "Descripción", 25.0, 10, Categoria.HERRAMIENTAS)
"""