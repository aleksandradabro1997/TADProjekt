from robot import Robot
from environment import *
import pygame


pos = constants.get('robot_base')

if __name__ == '__main__':
    rob = [Robot(1, pos[0], pos[1]), Robot(2, pos[0], pos[1]), Robot(3, pos[0], pos[1])]
    env = [Shelf(1, 20, 200), Shelf(2, 120, 200), Shelf(3, 220, 200), Shelf(4, 320, 200), Shelf(5, 420, 200), Shelf(6, 520, 200)]
    charging_points = [ChargingPoint(1, 700, 30), ChargingPoint(2, 700, 120), ChargingPoint(4, 700, 220), ChargingPoint(5, 700, 320)]
    unload_points = [UnloadPoint(40, 550), UnloadPoint(140, 550), UnloadPoint(240, 550), UnloadPoint(340, 550), UnloadPoint(440, 550)]
    pygame.init()
    pygame.display.set_caption("Symulacja")
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))

    v = 0.5
    exit = False
    dir = [v, 0]
    dir1 = [v, 0]
    dir2 = [0, v]
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        screen.fill(constants.get('screen_color'))
        for x in rob:
            x.draw(screen)
        for x in env:
            x.draw(screen)
        for x in charging_points:
            x.draw(screen)
        for x in unload_points:
            x.draw(screen)
        rob[0].move_forward()
        rob[1].move_back()
        rob[2].move_left()

        pygame.display.flip()

    pygame.quit()

