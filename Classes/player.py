import pygame
from .constants import *

class Player:
    
    def __init__(self, win):
        self.image = CHARACTER_PIC
        self.win = win
        
        x = 200 - self.image.get_width() // 2
        y = self.win.get_height() // 2
        y = y - self.image.get_height() // 2

        self.center = (x, y)

    def draw(self):
        self.win.blit(self.image, self.center)