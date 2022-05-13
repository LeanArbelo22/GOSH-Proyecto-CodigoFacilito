import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(self.pos_x, self.pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = 5
        self.eat_sound = pygame.mixer.Sound('Sounds/eating.wav')        
        
    def draw_player(self, screen, ghost_img):
        screen.blit(ghost_img, self.rect)
        
    def left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
             
    def right(self):
        self.rect.x += self.speed
        if self.rect.x > (SIZE - PLAYER_WIDTH):
            self.rect.x = SIZE - PLAYER_WIDTH
        
    def up(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
            
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > PLAYER_FLOOR:
            self.rect.y = PLAYER_FLOOR


    