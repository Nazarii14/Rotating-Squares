import pygame
from colors import *
from square import Square
import numpy as np


class Drawer:
    def __init__(self, screen, sq_number):
        self.screen = screen
        self.sq_number = sq_number
        if sq_number == 2:
            self.squares = self.eval_squares()
        else:
            self.squares = self.eval_squares_1()

    def increase_sq_number(self):
        if self.sq_number <= 20:
            self.sq_number += 1
            if self.sq_number == 2:
                self.squares = self.eval_squares()
            else:
                self.squares = self.eval_squares_1()

    def decrease_sq_number(self):
        if self.sq_number > 1:
            self.sq_number -= 1
            if self.sq_number == 2:
                self.squares = self.eval_squares()
            else:
                self.squares = self.eval_squares_1()

    def eval_squares(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        min_dim = min(width, height)
        square_side = min_dim / 2
        halved_side = square_side / 2

        squares = [
            Square((halved_side, halved_side), halved_side * np.sqrt(2),
                   self.screen, COLORS[0], 1),
            Square((min_dim - halved_side, halved_side), halved_side * np.sqrt(2),
                   self.screen, COLORS[1]),
            Square((halved_side, min_dim - halved_side), halved_side * np.sqrt(2),
                   self.screen, COLORS[2]),
            Square((min_dim - halved_side, min_dim - halved_side), halved_side * np.sqrt(2),
                   self.screen, COLORS[3], 1)
        ]

        return squares

    def eval_squares_1(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        min_dim = min(width, height)
        square_side = min_dim / self.sq_number
        halved_side = square_side / 2

        squares = []

        direction = 0
        for i in range(self.sq_number):
            for j in range(self.sq_number):
                squares.append(Square(
                    (halved_side + i * square_side, halved_side + j * square_side),
                    halved_side * np.sqrt(2),
                    self.screen,
                    get_random_color(),
                    direction))
                if self.sq_number % 2 == 1:
                    direction = 1 - direction

        return squares

    def run(self):
        clock = pygame.time.Clock()

        running = True

        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for sq in self.squares:
                            if sq.clicked(mouse_x, mouse_y):
                                sq.change_color()
                    if event.button == 2:
                        self.increase_sq_number()
                    if event.button == 3:
                        for sq in self.squares:
                            sq.change_direction()

                elif event.type == pygame.KEYDOWN:
                    self.decrease_sq_number()

            for sq in self.squares:
                sq.draw()
                sq.rotate()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
