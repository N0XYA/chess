WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT = (255, 207, 159)
DARK = (210, 140, 69)

IMAGE_PATH = "resources/images/figures/"

SQUARE_WIDTH, SQUARE_HEIGHT = 60, 60

BOARD = [[(1 * SQUARE_WIDTH, 1 * SQUARE_HEIGHT)] * 8] * 8


INIT_FIGURES = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", ""],
                ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

BLACK_START_POSITIONS = [()]
WHITE_START_POSITIONS = []
