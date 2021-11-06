#!/usr/bin/env python3.9
"""
Implementación de principios SOLID

Versión de Python >=3.8
Autores: Dario Sotelo, Wilmer Siza, ....
Fecha: 06/11/2021
"""
from typing import Optional, NoReturn


class Coche:
    """
    Show anything
    """
    def __init__(self, marca):
        # type: (Optional[str]) -> NoReturn
        """
        Show anything
        """
        self.marca = marca

    def get_marca_coche(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        return self.marca


class CocheDB:
    """
    Show anything
    """
    def guardar_coche(self, coche):
        # type: (..., Coche) -> NoReturn
        """
        Show anything
        """
        pass

    def eliminar_coche(self, /, coche):
        # type: (..., Coche) -> NoReturn
        """
        Show anything
        """
        pass


coche = Coche('audi')

coche_db = CocheDB()
coche_db.guardar_coche(coche)
coche_db.eliminar_coche(coche)


"""
Output
"""