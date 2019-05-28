from shapely.geometry.polygon import Polygon
import pygame
from constants import *


class Object:
    def __init__(self, obj_id, x_pos=0, y_pos=0, length=10, width=10):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.width = width
        self.object_id = obj_id

    def move_right(self):
        if check_if_position_is_valid(self.x_pos, self.y_pos + 1):
            self.y_pos = self.y_pos + 1
        else:
            print('Size of the map is to small. Object cannot be moved')

    def move_left(self):
        if check_if_position_is_valid(self.x_pos, self.y_pos - 1):
            self.y_pos = self.y_pos - 1
        else:
            print('Size of the map is to small. Object cannot be moved')

    def move_forward(self):
        if check_if_position_is_valid(self.x_pos + 1, self.y_pos):
            self.x_pos = self.x_pos + 1
        else:
            print('Size of the map is to small. Object cannot be moved')

    def move_back(self):
        if check_if_position_is_valid(self.x_pos - 1, self.y_pos):
            self.x_pos = self.x_pos - 1
        else:
            print('Size of the map is to small. Object cannot be moved')

    def draw(self, screen):
            pass


class Shelf(Object):
    def __init__(self, obj_id, x_pos=13, y_pos=200, status=StatusesRack.CAN_BE_MOVED, length=25, width=300):
        Object.__init__(self, obj_id, x_pos, y_pos, length, width)
        self.status = status

        self.products = []
        for i in range(0, 7):
            self.products.append(Product((self.x_pos, self.y_pos - self.width / 2 + 50*i)))

        self.shelf = Polygon([(self.x_pos - self.length / 2, self.y_pos - self.width / 2),
                              (self.x_pos - self.length / 2, self.y_pos + self.width / 2),
                              (self.x_pos + self.length / 2, self.y_pos + self.width / 2),
                              (self.x_pos + self.length / 2, self.y_pos - self.width / 2)])

    def draw(self, screen):
        x, y = self.shelf.exterior.xy
        pygame.draw.polygon(screen, constants.get('shelf_color'), [(xx, yy) for xx, yy in zip(x, y)])
        for pr in self.products:
            pr.draw(screen)


class UnloadPoint:
    def __init__(self, x_pos, y_pos, length=40, width=40):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.width = width

        self.item = Polygon([(self.x_pos - self.length / 2, self.y_pos - self.width / 2),
                              (self.x_pos - self.length / 2, self.y_pos + self.width / 2),
                              (self.x_pos + self.length / 2, self.y_pos + self.width / 2),
                              (self.x_pos + self.length / 2, self.y_pos - self.width / 2)])

    def draw(self, screen):
        x, y = self.item.exterior.xy
        pygame.draw.polygon(screen, constants.get('unload_point_color'), [(xx, yy) for xx, yy in zip(x, y)])


class ChargingPoint(Object):
    def __init__(self, obj_id, x_pos=0, y_pos=0, length=40, width=40):
        Object.__init__(self, obj_id, x_pos, y_pos, length, width)
        self.status = StatusesChargingPoint.FREE
        self.item = Polygon([(self.x_pos - self.length / 2, self.y_pos - self.width / 2),
                            (self.x_pos - self.length / 2, self.y_pos + self.width / 2),
                            (self.x_pos + self.length / 2, self.y_pos + self.width / 2),
                            (self.x_pos + self.length / 2, self.y_pos - self.width / 2)])

    def draw(self, screen):
        x, y = self.item.exterior.xy
        pygame.draw.polygon(screen, constants.get('charging_point_color'), [(xx, yy) for xx, yy in zip(x, y)])

# We need to overwrite functions responsible for movement
    def move_forward(self):
        print('Charging point cannot be moved')
        pass

    def move_back(self):
        print('Charging point cannot be moved')
        pass

    def move_left(self):
        print('Charging point cannot be moved')
        pass

    def move_right(self):
        print('Charging point cannot be moved')
        pass

    def charge(self, robot):
        robot.status = StatusesRobot.CHARGING
        robot.power_left = constants.get('max_level')  # max level


class Order:
    def __init__(self, obj_id, size):
        self.obj_id = obj_id
        self.nb_of_items = size

    def remove_order(self):
        del self


class Product:
    def __init__(self, init_position=(13, 200), length=25, width=25):
        pos_x = init_position[0]
        pos_y = init_position[1]

        self.length = length
        self.width = width

        self.item = Polygon([(pos_x - self.length / 2, pos_y - self.width / 2),
                              (pos_x - self.length / 2, pos_y + self.width / 2),
                              (pos_x + self.length / 2, pos_y + self.width / 2),
                              (pos_x + self.length / 2, pos_y - self.width / 2)])

    def draw(self, screen):
        x, y = self.item.exterior.xy
        pygame.draw.polygon(screen, (255, 255, 0), [(xx, yy) for xx, yy in zip(x, y)])
