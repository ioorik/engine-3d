from engine_3d.interfaces.IShape import IShape
from engine_3d.interfaces.IWorld import IWorld


class World(IWorld):

    def __init__(
        self,
    ):
        self._shapes: list[IShape] = []

    @property
    def lShapes(self) -> list[IShape]:
        return self._shapes

    def add(self, shape: IShape):
        self._shapes.append(shape)
