from settings import *


class Figure():
    def __init__(self, x, y, team) -> None:
        self.x = x
        self.y = y
        self.team = team
        self.moves_counter = 0

    def move(self):
        pass


class Pawn(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/pawn_2x_ns.png"
    
    def move(self):
        if self.moves_counter == 0:
            self.y += 2 * SQUARE_HEIGHT
        else:
            self.y += SQUARE_HEIGHT
        self.moves_counter += 1



class Bishop(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/bishop_2x_ns.png"


class King(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/king_2x_ns.png"


class Knight(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/knight_2x_ns.png"


class Queen(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/queen_2x_ns.png"


class Rook(Figure):
    def __init__(self, x, y, team) -> None:
        super().__init__(x, y, team)
        self.img = IMAGE_PATH + f"{self.team}/rook_2x_ns.png"