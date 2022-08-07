import pygame
from .constants import *


class Game:

    def __init__(self, win):
        self.win = win

    def main_loop(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return False
        else:
            return True
