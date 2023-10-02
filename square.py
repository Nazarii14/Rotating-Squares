import pygame
import math
import numpy as np
from colors import get_random_color


class Square:
    def __init__(self, coords, side, screen, color, direction=0):
        self.x, self.y = coords
        self.side = side
        self.current_side = side
        self.screen = screen
        self.color = color
        self.angle = 0
        self.rotation_speed = math.pi / 360
        self.direction = direction

    def draw(self):
        verticles = []

        for i in range(4):
            point_coef = i * math.pi / 2
            starting_angle = 3 * math.pi / 4
            new_x = self.x + self.current_side * np.sin(self.angle + starting_angle + point_coef)
            new_y = self.y + self.current_side * np.cos(self.angle + starting_angle + point_coef)

            verticles.append((new_x, new_y))

        pygame.draw.polygon(self.screen, self.color, verticles)
        pygame.draw.line(self.screen, (255, 0, 0), (0, 400), (800, 400), 5)
        pygame.draw.line(self.screen, (255, 0, 0), (400, 0), (400, 800), 5)


    def rotate(self):
        if self.direction == 0:
            self.angle += self.rotation_speed
        else:
            self.angle -= self.rotation_speed
        self.current_side = self.side / (abs(math.cos(self.angle)) + abs(math.sin(self.angle)))
        self.angle %= (2 * math.pi)

    def change_direction(self):
        self.direction = 1 - self.direction

    def clicked(self, mouse_x, mouse_y):
        return (
                self.x - self.side <= mouse_x <= self.x + self.side and \
                self.y - self.side <= mouse_y <= self.y + self.side
        )

    def change_color(self):
        self.color = get_random_color()
