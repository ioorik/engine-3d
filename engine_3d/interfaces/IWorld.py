"""World is a virtual space that is composition of Shape objects:

This is an abstract interface:
    >>> IWorld()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class IWorld with abstract methods add, lShapes
"""

import abc

from engine_3d.interfaces.IShape import IShape


class IWorld(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, shape: IShape):
        """Add a shape to this world"""

    @property
    @abc.abstractmethod
    def lShapes(self) -> list[IShape]:
        """Return the list of contained shapes"""
