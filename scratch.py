import pygame as pg
import time
import numpy as np

BACKGROUND_COLOR = (10, 10, 10)
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

GRID_WIDTH = 10
GRID_HEIGHT = 10
CELL_SIZE = 10
sc_width = CELL_SIZE * GRID_WIDTH
sc_height = CELL_SIZE * GRID_HEIGHT  

if __name__ == "scratch":
