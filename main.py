import pygame
from Classes.constants import *
import sys

from Classes.game import Game

#FPS = 60

win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()

    game = Game(win)

    while running:
        clock.tick(FPS)
        
        running = game.main_loop()

        pygame.display.update()

main()