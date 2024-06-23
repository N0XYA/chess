import pygame
from pygame.locals import *
import time
import figures
from settings import *



def draw_board():
    x, y = 0, 0
    for i in range(len(BOARD)):
        for j in range(len(BOARD[i])):
            square = Rect(x, y, *BOARD[i][j])
            if i % 2 == 0:
                color = DARK
                if j % 2 == 0:
                    color = LIGHT
            else:
                color = LIGHT
                if j % 2 == 0:
                    color = DARK
            pygame.draw.rect(screen, color, square)
            x += SQUARE_WIDTH
        x = 0
        y += SQUARE_HEIGHT


pygame.init()
screen = pygame.display.set_mode((480, 480))
running = True


pawn = figures.Pawn(0, 0, team="black")
img = pygame.image.load(pawn.img)
img = pygame.transform.scale(img, (SQUARE_WIDTH, SQUARE_HEIGHT))
img.convert()
rect = img.get_rect()
rect.x += 2 * SQUARE_WIDTH
rect.y += 1 * SQUARE_HEIGHT
def render_figures():

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(GRAY)
        draw_board()
        screen.blit(img, rect)
        pygame.display.update()
pygame.quit()
