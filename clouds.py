import pygame, random
from pygame.math import Vector2
from constants import *

class Clouds():
    def __init__(self):
        self.random_location()
    
    def draw_clouds(self, screen, clouds_img):
        cloud_rect = pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        screen.blit(clouds_img, cloud_rect)
    
    def random_location(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10) 
        self.position = Vector2(self.x, self.y) 