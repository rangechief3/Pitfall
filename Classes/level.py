import pygame

from Classes.constants import CHARACTER_PIC, SKY_BLUE
from .player import Player


class Level:
    
    def __init__(self, win):
        self.win = win
        self.player = Player(win)
        self.draw()
        pass

    def move_player(self, direction):
        if direction == "jump":
            self.player.jump()
        elif direction == "left":
            self.player.move_left()
        elif direction == "right":
            self.player.move_right()

    def draw(self):
        self.win.fill(SKY_BLUE)
        self.player.draw()