"""

Usage example:

    >>> from engine_3d.World import World
    >>> world = World()
    >>> window = Window(world)
"""

import pygame

from engine_3d.interfaces.Point import Point
from engine_3d.interfaces.IWorld import IWorld


class Window:

    def __init__(
        self,
        world: IWorld,
        defaultColor: pygame.Color = pygame.Color(0xFF, 0xFF, 0xFF),
        gridSize: Point = Point(50, 50),
    ):
        self._world = world
        self._win: pygame.Surface = pygame.display.set_mode((500, 500))
        self._color = defaultColor
        self._gridSize = gridSize

    def draw(self):

        for i in range(self._win.get_width() // self._gridSize[0] + 1):

            pygame.draw.line(
                self._win,
                self._color,
                (i * self._gridSize[0], 0),
                (i * self._gridSize[0], self._win.get_height()),
                width=3,
            )

        for i in range(self._win.get_height() // self._gridSize[1] + 1):

            pygame.draw.line(
                self._win,
                self._color,
                (0, i * self._gridSize[1]),
                (self._win.get_width(), i * self._gridSize[1]),
                width=3,
            )

        for shape in self._world.lShapes:
            shape.draw(self._win, self._color)

        pygame.display.flip()
