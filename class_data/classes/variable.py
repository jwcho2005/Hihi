import pygame as pg

pg.init()

vec = pg.math.Vector2

g = vec(0, 350)
clock = pg.time.Clock()
FPS = 30
TIME = 1/FPS
SCREEN_SIZE = (1440, 810)
done = False
friction = 50

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

YELLOW = (255, 255, 0)
PURPLE = (80, 0, 80)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)