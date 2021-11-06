#!/usr/bin/env python3.9
"""
Implementación de principios SOLID

Versión de Python >=3.8
Autores: Dario Sotelo, Wilmer Siza, ....
Fecha: 06/11/2021
"""
import abc
from typing import NoReturn


class DataCleanInterface(abc.ABC):
    """
    Show anything
    """
    @abc.abstractmethod
    def remove_special_characters(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass


class IODataInterface(abc.ABC):
    """
    Show anything
    """
    @abc.abstractmethod
    def save_from_file(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass


class DataProcess(DataCleanInterface, IODataInterface):
    def save_from_file(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass

    def remove_special_characters(self):
        """
        Show anything
        """
        pass


print(issubclass(DataProcess, DataCleanInterface))
print(issubclass(DataProcess, IODataInterface))


"""
Output

True
True
"""