from shapely.geometry.point import Point
from shapely.affinity import rotate
import pygame
from environment import *


class Robot(Object):
    def __init__(self, obj_id, x_pos, y_pos, radius=15, status=StatusesRobot.FREE, power=constants.get('max_power'), shelf=Shelf(1)):
        Object.__init__(self, obj_id, x_pos, y_pos)
        self.radius = radius
        self.robShape = Point(x_pos, y_pos).buffer(1)
        self.status = status
        self.power_left = power
        self.shelf_held = shelf

    def draw(self, screen):
        pygame.draw.circle(screen, constants.get('robot_color'), [int(self.x_pos), int(self.y_pos)], self.radius)

    def move_right(self):
        Object.move_right(self)
        self.shelf_held.move_right()

    def move_left(self):
        Object.move_left(self)
        self.shelf_held.move_left()

    def move_back(self):
        Object.move_back(self)
        self.shelf_held.move_back()

    def move_forward(self):
        Object.move_forward(self)
        self.shelf_held.move_forward()

    def get_position(self):
        return [self.x_pos, self.y_pos]



