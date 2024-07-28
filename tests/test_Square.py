from engine_3d.interfaces.Point import Point
from engine_3d.shapes.Square import Square


class TestSquare:
    """Test Square"""

    def test___getitem__(self):
        """Verify nominal behavior of `__getitem__`"""
        square = Square(Point(1, 2), 5)
        assert square.position[0] == 1
        assert square.position[1] == 2
