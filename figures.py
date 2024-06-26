import pygame
from pygame.locals import *
from settings import *


class Figure():
    def __init__(self, x, y, team) -> None:
        self.x = x
        self.y = y
        self.team = team
        self.name = None
        self.img = None
        self.rect = None

    def draw_moves(self):
        pass

    def move(self):
       pass 
    
    def render_move(self, move, figures_coordinates):
        square_x = self.x + move[0]
        square_y = self.y + move[1]
        color = GREEN
        enemy_team = "black" if self.team == "white" else "white"
        if (square_x, square_y) in figures_coordinates[self.team]:
            color = BLUE
        elif (square_x, square_y) in figures_coordinates[enemy_team]:
            color = RED
        square = Rect(square_x * SQUARE_HEIGHT, square_y * SQUARE_HEIGHT, SQUARE_HEIGHT, SQUARE_HEIGHT)
        return color, square

    def render(self):
        i_width = SQUARE_WIDTH - IMAGE_OFFSET
        i_height = SQUARE_HEIGHT - IMAGE_OFFSET
        image = pygame.image.load(self.img).convert_alpha()
        image = pygame.transform.scale(image, (i_width, i_height))
        self.rect = image.get_rect()
        self.rect.center = SQUARE_WIDTH // 2, SQUARE_HEIGHT // 2
        self.rect.x += self.x * SQUARE_WIDTH
        self.rect.y += self.y * SQUARE_HEIGHT
        return image, self.rect


class Pawn(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Pawn"
        self.img = IMAGE_PATH + f"{self.team}/pawn_2x_ns.png"
        self.first_move = True

    def draw_moves(self, figures_coordinates):
        move_squares = []
        if self.team == "black":
            available_moves = [(0, 1), (0, 2)]
        else:
            available_moves = [(0, -1), (0, -2)]
        for move in available_moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares

class Bishop(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Bishop"
        self.img = IMAGE_PATH + f"{self.team}/bishop_2x_ns.png"

    def draw_moves(self, figures_coordinates):
        available_moves = []
        for i in range(1, 8):
            for j in range(1, 8):
                if i == j:
                    available_moves.append((i, j))
                    available_moves.append((-i, -j))
                    available_moves.append((i, -j))
                    available_moves.append((-i, j))
        move_squares = []
        for move in available_moves:
            move_squares.append(self.render_move(move, figures_coordinates))    
        return move_squares

class King(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "King"
        self.img = IMAGE_PATH + f"{self.team}/king_2x_ns.png"

    def draw_moves(self, figures_coordinates):
        move_squares = []
        available_moves = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for move in available_moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares

class Knight(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Knight"
        self.img = IMAGE_PATH + f"{self.team}/knight_2x_ns.png"

    def draw_moves(self, figures_coordinates):
        move_squares = []
        available_moves = [(1, 2), (-1, 2), (-1, -2), (1, -2)]
        for move in available_moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares

class Queen(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Queen"
        self.img = IMAGE_PATH + f"{self.team}/queen_2x_ns.png"

    def draw_moves(self, figures_coordinates):
        available_moves = []
        for i in range(1, 8):
            for j in range(1, 8):
                if i == j:
                    available_moves.append((i, j))
                    available_moves.append((-i, -j))
                    available_moves.append((i, -j))
                    available_moves.append((-i, j))
                    available_moves.append((0, j))
                    available_moves.append((0, -j))
            available_moves.append((i, 0))
            available_moves.append((-i, 0))      
        move_squares = []
        for move in available_moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares

class Rook(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Rook"
        self.img = IMAGE_PATH + f"{self.team}/rook_2x_ns.png"