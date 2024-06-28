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
        self.enemy_team = "black" if self.team == "white" else "white"

    def draw_moves(self):
        pass

    def move(self):
       pass 
    
    def render_move(self, move, figures_coordinates):
        square_x = self.x + move[0]
        square_y = self.y + move[1]
        color = GREEN
        if (square_x, square_y) in figures_coordinates[self.team]:
            color = BLUE
        elif (square_x, square_y) in figures_coordinates[self.enemy_team]:
            color = RED
        square = Rect(square_x * SQUARE_HEIGHT, square_y * SQUARE_HEIGHT, SQUARE_HEIGHT, SQUARE_HEIGHT)
        return color, square

    def render(self):
        image = pygame.image.load(self.img).convert_alpha()
        self.rect = image.get_rect()
        self.rect.center = SQUARE_WIDTH // 2, SQUARE_HEIGHT // 2
        self.rect.x += self.x * SQUARE_WIDTH
        self.rect.y += self.y * SQUARE_HEIGHT
        return image, self.rect
    
    def vertical(self, figures_coordinates):
        vertival_moves = []
        top_n = [self.x, -9]
        bot_n = [self.x, 9]
        for i in range(1, 8):
            if self.y - i >= 0:
                vertival_moves.append([0 + self.x, self.y - i])
            if self.y + i < 8:
                vertival_moves.insert(0, [0 + self.x, self.y + i])         
        for move in vertival_moves:
            if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                if move[1] < self.y and move[1] > top_n[1]:
                    top_n[1] = move[1]
                if move[1] > self.y and move[1] < bot_n[1]:
                    bot_n[1] = move[1]
        if top_n != [self.x, -9]:
            t_i = vertival_moves.index(top_n)
            vertival_moves = vertival_moves[:t_i]
            vertival_moves.append(top_n)
        if bot_n != [self.x, 9]:
            b_i = vertival_moves.index(bot_n)
            vertival_moves = vertival_moves[b_i:]
        for move in vertival_moves:
            move[0] -= self.x
            move[1] -= self.y
        return vertival_moves
        
    def horizontal(self, figures_coordinates):
        horizontal_moves = []
        left_n = [-9, self.y]
        right_n = [9, self.y]
        for i in range(1, 8):
            if i + self.x < 8:
                horizontal_moves.append([i + self.x, self.y])
            if -i + self.x >= 0:
                horizontal_moves.insert(0, [-i + self.x, self.y])
        for move in horizontal_moves:
            if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                if move[0] <= self.x and move[0] >= left_n[0]:
                    left_n[0] = move[0]
                elif move[0] >= self.x and move[0] <= right_n[0]:
                    right_n[0] = move[0]
        if left_n != [-9, self.y]:
            l_i = horizontal_moves.index(left_n)
            horizontal_moves = horizontal_moves[l_i:]
        if right_n != [9, self.y]:
            r_i = horizontal_moves.index(right_n)
            horizontal_moves = horizontal_moves[:r_i]
            horizontal_moves.append(right_n)
        for move in horizontal_moves:
            move[0] -= self.x
            move[1] -= self.y
        return horizontal_moves

    def diagonal(self, figures_coordinates):
        bot_right = []
        top_left = []
        top_right = []
        bot_left = []
        for i in range(1, 7):
            if self.x + i < 8 and self.y + i < 8:
                bot_right.append([self.x + i, self.y + i])
            if self.x - i >= 0 and self.y - i >= 0:
                top_left.append([self.x - i, self.y - i])
            if self.x + i < 8 and self.y - i >= 0:
                top_right.append([self.x + i, self.y - i])
            if self.x - i >= 0 and self.y + i < 8:
                bot_left.append([self.x - i, self.y + i])
        
        if bot_right:
            for move in bot_right:
                if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                    index = bot_right.index(move)
                    bot_right = bot_right[:index]
                    bot_right.append(move)
        if top_left:
            for move in top_left:
                if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                    index = top_left.index(move)
                    top_left = top_left[:index]
                    top_left.append(move)
        if top_right:
            for move in top_right:
                if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                    index = top_right.index(move)
                    top_right = top_right[:index]
                    top_right.append(move)
        if bot_left:
            for move in bot_left:
                if tuple(move) in figures_coordinates[self.team] or tuple(move) in figures_coordinates[self.enemy_team]:
                    index = bot_left.index(move)
                    bot_left = bot_left[:index]
                    bot_left.append(move)
        all_moves = bot_right + top_left + top_right + bot_left
        for move in all_moves:
            move[0] -= self.x
            move[1] -= self.y
        return all_moves
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
        moves = self.diagonal(figures_coordinates)
        move_squares = []
        for move in moves:
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
        moves = []
        moves += self.horizontal(figures_coordinates)    
        moves += self.vertical(figures_coordinates)
        moves += self.diagonal(figures_coordinates)
        move_squares = []
        for move in moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares


class Rook(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.name = "Rook"
        self.img = IMAGE_PATH + f"{self.team}/rook_2x_ns.png"

    def draw_moves(self, figures_coordinates):
        moves = []
        moves += self.horizontal(figures_coordinates)    
        moves += self.vertical(figures_coordinates)
        move_squares = []
        for move in moves:
            move_squares.append(self.render_move(move, figures_coordinates))
        return move_squares
