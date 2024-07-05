from settings import *

class Player():
    def __init__(self) -> None:
        self.figures = []

    def append_figures(self, figure):
        self.figures.append(figure)

    def render_figures(self, screen):
        for figure in self.figures:
            screen.blit(*figure.render())
    
    def delete_figures(self, coordinates):
        for figure in self.figures:
            if figure.get_coordinates() == tuple(coordinates):
                self.figures.remove(figure)

    def get_coords(self):
        coordinates = []
        for figure in self.figures:
            coordinates.append((figure.x, figure.y))
        return coordinates