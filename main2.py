import math as m
import sys
from collections import namedtuple

import pygame
from pygame import *
from pygame.display import *
from pygame.draw import *

pygame.init()

def square(surf, col, point1, point2, point3, point4):
    polygon(surf, col, ((point1, point2), (point2, point3), (point3, point4), (point4, point1)))

class wall:
    def __init__(self, surf: pygame.Surface, width: float, height: float, depth: float, x: float, y: float, z: float, col: pygame.color, playerPosition: list[float|float|float]):
        self.win: pygame.Surface = surf
        self.dim: list[float|float|float] = [width, height, depth]
        self.xyz: list[float|float|float] = self.convert3Dto2D([x, y, z])
        self.color: pygame.Color = col
        self.playerPos: list[float|float|float] = playerPosition
        self.rot: float = m.atan2(self.xyz[2] - self.playerPos[2], self.xyz[0] - self.playerPos[0])

        self.centerX: int = int(get_window_size()[0] / 2)
        self.centerY: int = int(get_window_size()[1] / 2)

Point = namedtuple("Point", "X Y")
def main():
    sizeX = 850
    sizeY = 650
    size = (sizeX, sizeY)
    win = set_mode(size)
    horizon = Point(sizeX / 2, sizeY / 2 + 100)
    rot = 0
    walls = (
        [(1, 1, 1), (1, 0, 1), (255, 255, 255)],
    )

    gridSize = 30
    yOffset = 5
    while True:
        win.fill((0, 0, 0))

        for e in event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        k = key.get_pressed()

        if k[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if k[K_UP]:
            yOffset = (yOffset +  0.1) % gridSize
        
        line(win, (255, 255, 255), (0, horizon.Y), (sizeX, horizon[1]))
        
        for i in range(sizeX // gridSize * -1, sizeX // gridSize):
            line(win, (255, 255, 255), (horizon[0], horizon[1]), (i * 100,  sizeY))

        for i in range(int(horizon[1]) // gridSize, sizeY):
            line(win, (255, 255, 255), (0, i * gridSize + yOffset), (sizeX, i * gridSize + yOffset))

        flip()


if __name__ == "__main__":
    main()
