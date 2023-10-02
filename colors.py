import numpy as np

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
SEA = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [YELLOW, RED, SEA, GREEN, BLUE]


def get_random_color():
    return (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
