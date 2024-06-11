"""

Usage example:
    >>> point = Point(5, 10)
    >>> point
    Point(x=5, y=10)
    >>> point + point
    Point(x=10, y=20)
    >>> point + Point(1, 0)
    Point(x=6, y=10)
    >>> point - Point(1, 0)
    Point(x=4, y=10)

    >>> tuple(point)
    (5, 10)

"""

from collections import namedtuple

_point = namedtuple("Point", ["x", "y"])
_point3D = namedtuple("Point3D", ["x", "y", "z"])


class Point:

    def __init__(self, x, y, z=None):
        if z is None:
            self._tupPoint = _point(x, y)
        else:
            self._tupPoint = _point3D(x, y, z)

    def __add__(self, other):
        assert isinstance(other, self.__class__)
        return self.__class__(
            *(sum(c) for c in list(zip(self._tupPoint, other._tupPoint)))
        )

    def __sub__(self, other):
        assert isinstance(other, self.__class__)
        return self.__class__(
            *(c - c_other for c, c_other in list(zip(self._tupPoint, other._tupPoint)))
        )

    def __iter__(self):
        for c in self._tupPoint:
            yield c

    def __repr__(self):
        return repr(self._tupPoint)

    def __getitem__(self, item):
        return self._tupPoint[item]
