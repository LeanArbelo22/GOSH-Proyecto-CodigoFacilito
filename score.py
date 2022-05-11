import pygame
from constants import *

class Score():
    def __init__(self):
        self.score_text = 0 # !!!
        
    def draw_score(self, game_font, screen):
        score_surface = game_font.render(str(self.score_text), False, SCORE_COLOR)
        score_x = int(CELL_SIZE + CELL_SIZE)
        score_y = int(CELL_SIZE + (CELL_SIZE / 2)) 
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)     
        line_rect = pygame.Rect(score_rect.left - 4, score_rect.top - 2, score_rect.width + 6, score_rect.height + 4)
        pygame.draw.rect(screen, SCORE_COLOR, line_rect, 2)