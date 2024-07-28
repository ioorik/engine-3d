import math as m
import sys
from collections import namedtuple

import pygame
from pygame import *
from pygame.display import *
from pygame.draw import *

pygame.init()


def square(surf, col, point1, point2, point3, point4):
    polygon(
        surf,
        col,
        ((point1, point2), (point2, point3), (point3, point4), (point4, point1)),
    )


class wall:
    def __init__(
        self,
        surf: pygame.Surface,
        width: float,
        height: float,
        depth: float,
        x: float,
        y: float,
        z: float,
        col: pygame.color,
        playerPosition: list[float | float | float],
    ):
        self.win: pygame.Surface = surf
        self.dim: list[float | float | float] = [width, height, depth]
        self.xyz: list[float | float | float] = self.convert3Dto2D([x, y, z])
        self.color: pygame.Color = col
        self.playerPos: list[float | float | float] = playerPosition
        self.rot: float = m.atan2(
            self.xyz[2] - self.playerPos[2], self.xyz[0] - self.playerPos[0]
        )

        self.centerX: int = int(get_window_size()[0] / 2)
        self.centerY: int = int(get_window_size()[1] / 2)


Point = namedtuple("Point", "X Y")
ColorTuple = namedtuple("Color", "R G B")


def main():
    sizeX = 850
    sizeY = 650
    win = set_mode((sizeX, sizeY))
    xHorizon_0 = sizeX / 2
    yHorizon_0 = sizeY / 2 + 100
    xHorizon = xHorizon_0
    defaultColor = ColorTuple(255, 255, 255)
    walls = ([(1, 1, 1), (1, 0, 1), defaultColor],)

    gridSize = 30
    xGridSize = yGridSize = gridSize
    xOffset = 0
    yOffset = 5
    velocity = 0.3
    while True:
        win.fill((0, 0, 0))
        yHorizon = yHorizon_0 + (xHorizon - xHorizon_0) ** 2 / 1000

        for e in event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        k = key.get_pressed()

        if k[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if k[K_UP]:
            yHorizon_0 -= velocity
        if k[K_DOWN]:
            yHorizon_0 += velocity
        if k[K_LEFT]:
            xHorizon = xHorizon + velocity
        if k[K_RIGHT]:
            xHorizon = xHorizon - velocity
        if k[K_d]:
            xOffset = (xOffset - velocity) % xGridSize
        if k[K_a]:
            xOffset = (xOffset + velocity) % xGridSize
        if k[K_w]:
            yOffset = (yOffset + velocity) % yGridSize
        if k[K_s]:
            yOffset = (yOffset - velocity) % yGridSize

        yGridSize = max(int(round(gridSize * (sizeY - yHorizon) / sizeY * 2)), 1)

        line(win, defaultColor, (0, yHorizon), (sizeX, yHorizon))

        xDrift = 10 * sizeX
        for i in range(-xDrift, sizeX + xDrift + 1, xGridSize):
            _xEndPosition = i + xOffset
            # print(_xEndPosition)
            line(win, defaultColor, (xHorizon, yHorizon), (_xEndPosition, sizeY))

        for i in range(int(yHorizon), sizeY + 1, yGridSize):
            line(win, defaultColor, (0, i + yOffset), (sizeX, i + yOffset))

        flip()


if __name__ == "__main__":
    main()
