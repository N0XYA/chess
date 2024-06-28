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
        

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))


pygame.init()
pygame.display.set_caption("Chess")
icon = pygame.image.load(GAME_ICON)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 64)
running = True
moving = False
bplayer = player.Player()
wplayer = player.Player()
font = pygame.font.SysFont("Arial" , 18 , bold = True)
selected = None
selected_moves = None
running = True
clock = pygame.time.Clock()

init_figures()

while running:
    coordinates = {
        "black": bplayer.get_coords(),
        "white": wplayer.get_coords()
    }
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                selected = None
                selected_moves = None
            elif event.button == 1:
                for figure in bplayer.figures:
                    if figure.rect.collidepoint(event.pos):
                        selected = f"Selected {figure.name}"                
                        selected_moves = figure.draw_moves(coordinates)
                for figure in wplayer.figures:
                    if figure.rect.collidepoint(event.pos):
                        selected_moves = figure.draw_moves(coordinates)
        
        screen.fill(GRAY)
        draw_board()
        if selected_moves is not None:
            for move in selected_moves:
                pygame.draw.rect(screen, *move)
        wplayer.render_figures(screen)
        bplayer.render_figures(screen)
        fps_counter()
        pygame.display.update()
        clock.tick(60)
pygame.quit()

