import sys

import pygame

from engine_3d.Window import Window
from engine_3d.interfaces.Point import Point
from engine_3d.shapes.Square import Square
from engine_3d.shapes.Triangle import Triangle

pygame.init()


class Player:

    def __init__(
        self,
        sizeX: int,
        sizeY: int,
        defaultColor: pygame.Color = (255, 255, 255),
        backgroundColor: pygame.Color = (0, 0, 0),
        caption: str = "3D Game engine",
    ):
        self.screenSizeX: int = sizeX
        self.screenSizeY: int = sizeY
        self.running = True
        self.defCol = defaultColor
        self.bgCol = backgroundColor

        self.win: pygame.Surface = pygame.display.set_mode(
            (self.screenSizeX, self.screenSizeY)
        )
        pygame.display.set_caption(caption)

        self.rot: float | int = 0
        self.canTurnA = True
        self.canTurnD = True

        self.gridSizeX = 30
        self.gridSizeY = 50

        self.gameLoop()

    def gameLoop(self):
        self.win.fill(self.bgCol)

        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.running = False

            self.movement(keys)

            window = Window(
                self.win,
                pygame.Color(255, 255, 255),
                self.gridSizeX,
                self.gridSizeY,
            )
            if mouse[0]:
                mousePos = pygame.mouse.get_pos()
                window.addShape(
                    Square(
                        Point(
                            mousePos[0] // self.gridSizeX, mousePos[1] // self.gridSizeY
                        ),
                        1,
                        self.gridSizeX,
                        self.gridSizeY,
                    )
                )

            if mouse[2]:
                mousePos = pygame.mouse.get_pos()

                window.addShape(
                    Triangle(
                        Point(
                            mousePos[0] // self.gridSizeX, mousePos[1] // self.gridSizeY
                        ),
                        1,
                        self.gridSizeX,
                        self.gridSizeY,
                        self.rot,
                    )
                )

            window.draw()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def movement(self, keys):
        if keys[pygame.K_a] and self.canTurnA:
            self.rot -= 90
            self.canTurnA = False
        if keys[pygame.K_d] and self.canTurnD:
            self.rot += 90
            self.canTurnD = False
        if not keys[pygame.K_a]:
            self.canTurnA = True
        if not keys[pygame.K_d]:
            self.canTurnD = True


if __name__ == "__main__":
    player1 = Player(800, 700)
