import pygame
import sys
import random
import math

screen_width = 800
screen_height = 800

BLUE = (0, 0, 255)
GREEN = (0, 225, 0)
RED = (225, 0, 0)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((screen_width, screen_height))


class Game:
    def __init__(self, blue=(700, 750), red=(50, 50), green=(350, 350), white=(650, 250), blue_score=0, red_score=0):
        self.blue = blue
        self.red = red
        self.green = green
        self.white = white
        self.blue_score = blue_score
        self.red_score = red_score
    def move(self):
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_a]:
            self.red[1] -= 1
        if key_event[pygame.K_d]:
