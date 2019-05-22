from shapely.geometry.point import Point
from shapely.affinity import rotate
import pygame


class Robot:
    def __init__(self, init_position=(250, 200), radius=15):
        self.radius = radius
        pos_x = init_position[0]
        pos_y = init_position[1]
        self.position = [pos_x, pos_y]
        self.robShape = Point(pos_x, pos_y).buffer(1)

    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,255), [int(self.position[0]), int(self.position[1])], self.radius)

    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y

    def getPosition(self):
        return self.position

