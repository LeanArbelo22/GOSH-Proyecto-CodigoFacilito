import pygame 
from random import randint
from pygame.math import Vector2
from constants import *

class Clouds():
    def __init__(self):
        self.random_location()
        self.speed = -0.008
    
    def draw_clouds(self, screen, clouds_img):
        cloud_rect = pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        screen.blit(clouds_img, cloud_rect)
    
    def random_location(self):
        self.x = randint(0, 10)
        self.y = randint(0, 10) 
        self.position = Vector2(self.x, self.y) 
        
    def move_clouds(self):
        self.position.x += self.speed
        # self.position.y -= self.speed
        if self.position.x < -20:
            self.speed = 0.008
        elif self.position.x > 20:
            self.speed = -0.008
        