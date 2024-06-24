import pygame
from pygame.locals import *
import time
import figures
import player
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

def init_figures():
    for i in range(len(INIT_FIGURES)):
        for j in range(len(INIT_FIGURES[i])):
            if INIT_FIGURES[i][j] == "":
                continue
            color_letter = INIT_FIGURES[i][j][0]
            color = "black" if color_letter == "b" else "white"
            match INIT_FIGURES[i][j][1]:
                case 'r':
                    rook = figures.Rook(j, i, color)
                    if color == "black":
                        bplayer.append_figures(rook)
                    else:
                        wplayer.append_figures(rook)
                case 'n':
                    knight = figures.Knight(j, i, color)
                    if color == "black":
                        bplayer.append_figures(knight)
                    else:
                        wplayer.append_figures(knight)
                case 'b':
                    bishop = figures.Bishop(j, i, color)
                    if color == "black":
                        bplayer.append_figures(bishop)
                    else:
                        wplayer.append_figures(bishop)
                case 'q':
                    queen = figures.Queen(j, i, color)
                    if color == "black":
                        bplayer.append_figures(queen)
                    else:
                        wplayer.append_figures(queen)
                case 'k':
                    king = figures.King(j, i, color)
                    if color == "black":
                        bplayer.append_figures(king)
                    else:
                        wplayer.append_figures(king)
                case 'p':
                    pawn = figures.Pawn(j, i, color)
                    if color == "black":
                        bplayer.append_figures(pawn)
                    else:
                        wplayer.append_figures(pawn)
        

pygame.init()
screen = pygame.display.set_mode((480, 480))
running = True

bplayer = player.Player()
wplayer = player.Player()

init_figures()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(GRAY)
        draw_board()
        wplayer.render_figures(screen)
        bplayer.render_figures(screen)
        pygame.display.update()
pygame.quit()
