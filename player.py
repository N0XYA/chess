import pygame
from settings import *

class Player():
    def __init__(self) -> None:
        self.figures = []

    def append_figures(self, figure):
        self.figures.append(figure)

    def render_figures(self, screen):
        for figure in self.figures:
            i_width = SQUARE_WIDTH - 15
            i_height = SQUARE_HEIGHT - 15
            image = pygame.image.load(figure.img)
            image = pygame.transform.scale(image, (i_width, i_height))
            image.convert()
            rect = image.get_rect()
            rect.center = SQUARE_WIDTH // 2, SQUARE_HEIGHT // 2
            rect.x += figure.x * SQUARE_WIDTH
            rect.y += figure.y * SQUARE_HEIGHT
            screen.blit(image, rect)