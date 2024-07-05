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
screen.set_alpha(128)
running = True
bplayer = player.Player()
wplayer = player.Player()
font = pygame.font.SysFont("Arial" , 18 , bold = True)

selected_figure = None
selected_moves = None
move_coords = None
color = None
enemy_coordinates = None
clock = pygame.time.Clock()

turn = "white"
running = True

init_figures()

while running:
    coordinates = {
        "black": bplayer.get_coords(),
        "white": wplayer.get_coords()
    }
    player = wplayer if turn == "white" else bplayer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                selected_figure = None
                selected_moves = None
                enemy_coordinates = None
            elif event.button == 1:
                for figure in player.figures:
                    if figure.rect.collidepoint(event.pos):
                        selected_figure = figure
                        selected_moves, move_coords = figure.draw_moves(coordinates)
                        coordinates[turn] = player.get_coords()
                        break
                if selected_figure is not None:
                    for i in range(len(move_coords)):
                        if selected_moves[i][1].collidepoint(event.pos):
                            color, enemy_coordinates = selected_figure.move(move_coords[i], coordinates)
                            if enemy_coordinates is not None:
                                bplayer.delete_figures(enemy_coordinates) if turn == "white" else wplayer.delete_figures(enemy_coordinates)
                                coordinates[turn] = player.get_coords()
                                enemy_coordinates = None
                                color = None
                            selected_moves = None
                            selected_figure = None
                            turn = "white" if turn == "black" else "black"
                            break
        screen.fill(GRAY)
        draw_board()
        if selected_moves is not None:
            for move in selected_moves:
                pygame.draw.rect(screen, *move, -1 if move[0] == GREEN else 0)
        if selected_figure is not None:
            pygame.draw.rect(screen, GREEN,  (selected_figure.x * SQUARE_HEIGHT, selected_figure.y * SQUARE_HEIGHT, SQUARE_HEIGHT, SQUARE_HEIGHT))
        wplayer.render_figures(screen)
        bplayer.render_figures(screen)
        fps_counter()
        which_turn = font.render(turn , 1, pygame.Color(BLACK))
        screen.blit(which_turn ,(480,0))
        pygame.display.update()
        clock.tick(60)
pygame.quit()

