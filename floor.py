import pygame
import pygame
from constants import *

# Floor Rect
class Floor():
    def __init__(self, pos_x, pos_y):
        self.floor_image = pygame.Surface( (CELL_SIZE * CELL_NUMBER, CELL_SIZE * 2) )
        self.floor_image.fill(GRASS_COLOR1)
        self.floor_rect = self.floor_image.get_rect()
        self.floor_rect.x = pos_x
        self.floor_rect.y = pos_y
        
    def draw_floor(self, screen):
        # Grid 
        for row in range(CELL_SIZE): # Vertical fields
            if row % 2 == 0:
                for column in range(CELL_NUMBER): # Horizontal fields
                    if column % 2 == 0: # Pair positions
                        grass_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.floor_image, GRASS_COLOR2, grass_rect)
        
        for row in range(CELL_SIZE):
            if row % 2 != 0:
                for column in range(CELL_NUMBER):
                    if column % 2 != 0: # Odd positions
                        grass_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.floor_image, GRASS_COLOR2, grass_rect)
        
        screen.blit(self.floor_image, self.floor_rect)