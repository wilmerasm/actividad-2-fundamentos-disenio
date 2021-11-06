#!/usr/bin/env python3.9
"""
Implementación de principios SOLID

Versión de Python >=3.8
Autores: Dario Sotelo, Wilmer Siza, ....
Fecha: 06/11/2021
"""
import abc
from typing import Any, NoReturn


class DBContext(abc.ABC):
    """
    Show anything
    """
    @abc.abstractmethod
    def get_data(self): pass

    @abc.abstractmethod
    def set_data(self): pass


class DataManager:
    """
    Show anything
    """
    def __init__(self, context):
        # type: (Any) -> NoReturn
        """
        Show anything
        """
        self.__context = context


class UserManager(DBContext):
    def get_data(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass

    def set_data(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass


class APIManager(DBContext):
    def get_data(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass

    def set_data(self):
        # type: () -> NoReturn
        """
        Show anything
        """
        pass


print(DataManager(None)._DataManager__context)
print(issubclass(UserManager, DBContext))
print(issubclass(APIManager, DBContext))


"""
Output

None
True
True
"""