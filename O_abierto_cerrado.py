#!/usr/bin/env python3.9
"""
Implementación de principios SOLID

Versión de Python >=3.8
Autores: Dario Sotelo, Wilmer Siza, ....
Fecha: 06/11/2021
"""
from typing import List, NoReturn
import abc


class Coche:
    """
    Show anything
    """
    def __init__(self, marca, precio):
        # type: (str, int) -> NoReturn
        """
        Show anything

        :param marca:
        :param precio:
        """
        self.marca = marca
        self.precio = precio

    def get_marca_coche(self):
        # type: () -> str
        """
        Show anything

        :return marca:
        """
        return self.marca


class CocheDos(abc.ABC):
    """
    Show anything
    """
    @abc.abstractmethod
    def precio_medio_coche(self):
        """
        Show anything
        """
        pass


class Renault(CocheDos):
    """
    Show anything
    """
    def precio_medio_coche(self):
        """
        Show anything

        :return precio:
        """
        return 18000


class Audi(CocheDos):
    """
    Show anything
    """
    def precio_medio_coche(self):
        """
        Show anything

        :param precio:
        """
        return 25000


class Mercedes(CocheDos):
    """
    Show anything
    """
    def precio_medio_coche(self):
        """
        Show anything

        :return precio:
        """
        return 27000


def imprimir_precio_medio_coche(coches: List[Coche]):
    """
    Show anything

    :param coches:
    """
    for coche in coches:
        if coche.marca == 'Renault':
            print(coche.precio)
        if coche.marca == 'Audi':
            print(coche.precio)


def imprimir_precio_medio_coche_dos(coches: List):
    """
    Show anything

    :param coches:
    """
    for coche in coches:
        print(coche.precio_medio_coche())


if __name__ == '__main__':
    coches = [
        Coche('Renault', 18000),
        Coche('Audi', 25000)
    ]

    coches_dos = [
        Renault(),
        Audi(),
        Mercedes()
    ]
    print("Ejemplo 1:")
    imprimir_precio_medio_coche(coches)
    print("\nEjemplo 2:")
    imprimir_precio_medio_coche_dos(coches_dos)


"""
Output

Ejemplo 1:
18000
25000

Ejemplo 2:
18000
25000
27000
"""
