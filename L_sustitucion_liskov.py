#!/usr/bin/env python3.9
"""
Implementación de principios SOLID

Versión de Python >=3.8
Autores: Dario Sotelo, Wilmer Siza, ....
Fecha: 06/11/2021
"""
import abc
from typing import List, NoReturn


class Coche(abc.ABC):
    """
    Show anything
    """
    @abc.abstractmethod
    def num_asientos(self):
        """
        Show anything
        """
        pass


class Renault(Coche):
    """
    Show anything
    """
    def num_asientos(self):
        # type: () -> int
        """
        Show anything

        :return precio:
        """
        return 5


class Audi(Coche):
    """
    Show anything
    """
    def num_asientos(self):
        # type: () -> int
        """
        Show anything

        :param precio:
        """
        return 2


class Mercedes(Coche):
    """
    Show anything
    """
    def num_asientos(self):
        # type: () -> int
        """
        Show anything

        :return precio:
        """
        return 4


class Ford(Coche):
    """
    Show anything
    """
    def num_asientos(self):
        # type: () -> int
        """
        Show anything

        :return precio:
        """
        return 2


def imprimir_num_asientos(coches: List[Coche]):
    for coche in coches:
        print(f'Marca: {coche.__class__.__name__} Asientos: {coche.num_asientos()}')


if __name__ == '__main__':
    coches = [
        Renault(),
        Audi(),
        Mercedes(),
        Ford()
    ]
    imprimir_num_asientos(coches)


"""
Output

Marca: Renault Asientos: 5
Marca: Audi Asientos: 2
Marca: Mercedes Asientos: 4
Marca: Ford Asientos: 2
"""