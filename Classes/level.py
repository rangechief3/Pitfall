import pygame

from Classes.constants import *
from .player import Player


class Level:
    
    def __init__(self, win):
        self.clock = pygame.time.Clock()
        self.win = win
        self.player = Player(win)
        self.draw()
        self.standing_spot = self.win.get_height() // 2
        pass

    def move_player(self, direction):
        if direction == "jump":
            self.jump_loop()
        elif direction == "left":
            self.player.move_left()
        elif direction == "right":
            self.player.move_right()

    def jump_loop(self):
        jumping = True

        while jumping:
            self.clock.tick(FPS)

            self.player.jump()
            if self.player.center[1] >= self.standing_spot:
                jumping = False
                self.player.center = (self.player.center[0], self.standing_spot)
                self.player.launch = PLAYER_LAUNCH

            self.draw()
            pygame.display.update()



    def draw(self):
        self.win.fill(SKY_BLUE)
        self.player.draw()