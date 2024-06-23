import pygame
from pygame.locals import *
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

WIDTH, HEIGHT = 40, 40

BOARD = [[(1 * WIDTH, 1 * HEIGHT)] * 8] * 8


def draw_board():
    x, y = 0, 0
    for i in range(len(BOARD)):
        for j in range(len(BOARD[i])):
            square = Rect(x, y, *BOARD[i][j])
            if i % 2 == 0:
                color = BLACK
                if j % 2 == 0:
                    color = WHITE
            else:
                color = WHITE
                if j % 2 == 0:
                    color = BLACK
            pygame.draw.rect(screen, color, square)
            x += WIDTH
        x = 0
        y += HEIGHT


pygame.init()
screen = pygame.display.set_mode((720, 480))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(GRAY)
        draw_board()
        pygame.display.flip()
pygame.quit()

draw_board()