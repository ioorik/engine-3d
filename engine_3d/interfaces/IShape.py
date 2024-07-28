"""Shape desc TODO:

This is an abstract interface:
    >>> IShape()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class IShape with abstract methods draw, move, position
"""

import abc

import pygame

from engine_3d.interfaces.Point import Point


class IShape(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def position(self) -> Point:
        """Return current position"""

    @abc.abstractmethod
    def move(self, dp: Point):
        """Move 'delta point' relative to current location"""

    @abc.abstractmethod
    def draw(
        self,
        surface: pygame.Surface,
        color: pygame.Color,
    ):
        """Draw this shape in the provided surface"""
