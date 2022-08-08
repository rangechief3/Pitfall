import pygame
from .constants import *
from .level import Level

class Game:

    def __init__(self, win):
        self.level = Level(win)
        self.win = win
        self.clock = pygame.time.Clock()

    def main_loop(self):
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return False
        
        if keys[pygame.K_UP]:
            self.level.move_player("jump")
        elif keys[pygame.K_LEFT]:
            self.level.move_player("left")
        elif keys[pygame.K_RIGHT]:
            self.level.move_player("right")

        self.level.draw()
        return True
