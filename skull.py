import pygame
from random import randint
from constants import *

class Skulls(pygame.sprite.Sprite):
    def __init__(self, skull_img, skull_group, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = randint(0, (SIZE - CELL_SIZE))
        self.pos_y = randint(-1000, CELL_SIZE) 
        self.rect = pygame.Rect(self.pos_x, self.pos_y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.skull_img = skull_img
        self.skull_group = skull_group
        self.speed = speed
    
    def draw_skulls(self, screen):
        screen.blit(self.skull_img, self.rect)
                
    def dropping(self, speed):
        self.rect.y += speed 
    
                
        
        