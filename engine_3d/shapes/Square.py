"""Generic square shape on arbitrary world

Usage example:

    >>> square = Square(Point(10,20), 10)
    >>> square.position
    Point(x=10, y=20)
    >>> square._points
    [Point(x=10, y=20), Point(x=20, y=20), Point(x=20, y=30), Point(x=10, y=30)]
    >>> square.move(Point(1,0))
    >>> square.position
    Point(x=11, y=20)
    >>> square._points
    [Point(x=11, y=20), Point(x=21, y=20), Point(x=21, y=30), Point(x=11, y=30)]
"""

from engine_3d.interfaces.Point import Point
from engine_3d.bases.PolygonBase import PolygonBase


class Square(PolygonBase):
    def __init__(
        self,
        position: Point,
        size: float | int,
    ):
        """Generic square shape on arbitrary world

        :param position: Point of negative-most coordinates of the required square shape in virtual space
        :param size: Size of each dimension in virtual space
        """
        super().__init__(
            [
                position,
                Point((position[0] + size), position[1]),
                Point(*[(p + size) for p in position]),
                Point(position[0], position[1] + size),
            ],
        )
