import pygame
from constants import *

class Score():
    def __init__(self):
        self.score_text = 0 # !!!
        
    def draw_score(self, game_font, screen):
        self.score_surface = game_font.render(str(self.score_text), False, SCORE_COLOR)
        self.score_x = int(CELL_SIZE * 2)
        self.score_y = int(CELL_SIZE + (CELL_SIZE / 2)) 
        self.score_rect = self.score_surface.get_rect(center = (self.score_x, self.score_y))
        self.line_rect = pygame.Rect(self.score_rect.left - 4, self.score_rect.top - 2, self.score_rect.width + 6, self.score_rect.height + 4)
        pygame.draw.rect(screen, SCORE_COLOR, self.line_rect, 2)
        screen.blit(self.score_surface, self.score_rect)     
        
    def draw_best_score(self, game_font, screen, best_score):
        self.score_surface = game_font.render(str(best_score), False, SCORE_COLOR)
        self.score_x = int(SIZE - (CELL_SIZE * 4))
        self.score_y = int(CELL_SIZE + (CELL_SIZE / 2)) 
        self.score_rect = self.score_surface.get_rect(center = (self.score_x, self.score_y))
        screen.blit(self.score_surface, self.score_rect)   