import pygame

from engine_3d.interfaces.Point import Point
from engine_3d.bases.PolygonBase import PolygonBase


class Triangle(PolygonBase):

    def __init__(
        self,
        position: Point,
        size: float | int,
        gridSizeX: int,
        gridSizeY: int,
        angle: int,
    ):
        self._gridSizeX = gridSizeX
        self._gridSizeY = gridSizeY
        self._position = position
        self.rot = angle
        super().__init__(
            self._position,
            [Point(0, 0), Point(0, gridSizeY), Point(gridSizeX, gridSizeY)],
        )

    def draw(
        self,
        surface: pygame.Surface,
        color: pygame.Color,
    ):
        surf = pygame.Surface(
            (self._gridSizeX - 1, self._gridSizeY - 1)
        ).convert_alpha()
        super().draw(surf, color)
        rotSurf = pygame.transform.rotate(surf, self.rot)
        surface.blit(
            rotSurf,
            (
                self._position[0] * self._gridSizeX + 1,
                self._position[1] * self._gridSizeY + 1,
            ),
        )
