import pygame
from .constants import *

class Player:
    
    def __init__(self, win):
        self.image = CHARACTER_PIC
        self.win = win
        self.clock = pygame.time.Clock()
        self.launch = PLAYER_LAUNCH

        x = 200 - self.image.get_width() // 2
        y = self.win.get_height() // 2
        y = y - self.image.get_height() // 2

        self.center = (x, y)

    def move_left(self):
        x = self.center[0]
        x -= 5
        if x <= 0:
            self.center = (0, self.center[1])
        else:
            self.center = (x, self.center[1])

    def move_right(self):
        edge = self.win.get_width() - self.image.get_width()

        x = self.center[0]
        x += 5
        
        if x >= edge:
            self.center = (edge, self.center[1])
        else:
            self.center = (x, self.center[1])

    def jump(self):
        x, y = self.center

        y -= self.launch
        self.launch -= 10
        self.center = (x, y)

    def draw(self):
        self.win.blit(self.image, self.center)