from shapely.geometry.polygon import Polygon
import pygame


class Shelf:
    def __init__(self, init_position=(13, 200), length = 25, width = 300):
        pos_x = init_position[0]
        pos_y = init_position[1]

        self.length = length
        self.width = width

        self.products = []
        for i in range(0,7):
            self.products.append(Product((pos_x,pos_y - self.width / 2 + 50*i)))



        self.shelf = Polygon([(pos_x - self.length / 2, pos_y - self.width / 2),
                              (pos_x - self.length / 2, pos_y + self.width / 2),
                              (pos_x + self.length / 2, pos_y + self.width / 2),
                              (pos_x + self.length / 2, pos_y - self.width / 2)])

    def draw(self, screen):
        x, y = self.shelf.exterior.xy
        pygame.draw.polygon(screen, (255, 0, 255), [(xx, yy) for xx, yy in zip(x, y)])
        for pr in self.products:
            pr.draw(screen)

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

class UnloadPoint:
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
        pygame.draw.polygon(screen, (255, 128, 0), [(xx, yy) for xx, yy in zip(x, y)])