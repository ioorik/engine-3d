import time

import pygame
from pygame import display

from engine_3d.Window import Window
from engine_3d.World import World
from engine_3d.interfaces.Point import Point
from engine_3d.shapes.Square import Square


class TestWindow:
    """Test for `Window` class"""

    def test_uc_simple(self):
        """Verify simple usage"""
        pygame.init()
        world = World()
        window = Window(world)
        world.add(Square(Point(1, 2), size=0.1))
        world.add(Square(Point(3, 4), size=200.5))
        window.draw()
        time.sleep(5)
