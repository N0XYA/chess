WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT = (255, 207, 159)
DARK = (210, 140, 69)
GREEN = (153, 255, 153)
RED = (255, 102, 102)
BLUE = (153, 204, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
GAME_ICON = "resources/images/icon.png"
IMAGE_PATH = "resources/images/figures/scaled/"
IMAGE_OFFSET = 0

SQUARE_WIDTH, SQUARE_HEIGHT = 60, 60

BOARD = [[(SQUARE_WIDTH, SQUARE_HEIGHT)] * 8] * 8


INIT_FIGURES = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
