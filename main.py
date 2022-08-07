import pygame
from Classes.constants import *
import sys

#FPS = 60

win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.init()
screen_width = 1200
screen_height = 700
# screen = pygame.display.set_mode((screen_width,screen_height))



def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main()