from robot import Robot
from environment import Shelf
import pygame

if __name__ == '__main__':
    rob = [Robot((20, 380)), Robot((70, 20)), Robot((220, 20))]
    env = [Shelf((20, 200)),  Shelf((120, 200)),  Shelf((220, 200)),  Shelf((320, 200)),  Shelf((420, 200)), Shelf((520, 200))]
    pygame.init()
    pygame.display.set_caption("Symulacja")
    window_width = 600
    window_height = 400
    screen = pygame.display.set_mode((window_width, window_height))

    v = 0.5
    exit = False
    dir = [v,0]
    dir1 = [v, 0]
    dir2 = [0, v]
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        screen.fill((0, 0, 0))
        for x in rob:
            x.draw(screen)
        for x in env:
            x.draw(screen)
        rob[2].move(dir[0], dir[1])
        robPos = rob[2].getPosition()
        if robPos[0] > 570:
            dir = [-v, 0]
        elif robPos[0] < 170:
            dir = [v, 0]

        rob[0].move(dir1[0], dir1[1])
        robPos = rob[0].getPosition()
        if robPos[0] > 570:
            dir1 = [-v, 0]
        elif robPos[0] < 20:
            dir1 = [v, 0]

        rob[1].move(dir2[0], dir2[1])
        robPos = rob[1].getPosition()
        if robPos[1] > 370:
            dir2 = [0, -v]
        elif robPos[1] < 20:
            dir2 = [0, v]

        pygame.display.flip()

    pygame.quit()

