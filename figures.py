import pygame

class pawn():
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.img = f"resources/images/figures/{team}/pawn_2x_ns.png"
