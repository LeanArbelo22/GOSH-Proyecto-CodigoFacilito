from re import S
import pygame
from constants import *

class Decorator():
    def __init__(self, decorator_img):
        self.image = decorator_img
        self.rect = pygame.Rect(CELL_SIZE * 15, (PLAYER_FLOOR + (CELL_SIZE * 1.5)), DECORATION_WIDTH, DECORATION_HEIGHT)
    
    def draw_decorator(self, screen):
        screen.blit(self.image, self.rect)