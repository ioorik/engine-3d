"""Generic polygon shape on arbitrary world

Usage example:

    >>> poly = PolygonBase([Point(10,20)])
    >>> poly.position
    Point(x=10, y=20)
    >>> poly.move(Point(1,0))
    >>> poly.position
    Point(x=11, y=20)

"""

import pygame

from engine_3d.interfaces.Point import Point
from engine_3d.interfaces.IShape import IShape


class PolygonBase(IShape):

    def __init__(
        self,
        points: list[Point],
    ):
        self._points: list[Point] = points

    @property
    def position(self) -> Point:
        return self._points[0]

    def move(self, dp: Point):
        self._points = [p + dp for p in self._points]

    def draw(
        self,
        surface: pygame.Surface,
        color: pygame.Color,
    ):

        points = tuple(tuple(point) for point in self._points)

        pygame.draw.polygon(surface, color, points)
