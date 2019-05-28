import constants
from environment import *
from robot import *
# As an input we have matrix of 1 and 0. Zero means that there is no obstacles and 1 means there is an obstacle


def initialize_matrix_for_robot(map_width, map_length, shelf_pos, charging_pos, unload_pos):
    n = int(map_width/constants.get('robot_radius'))
    m = int(map_length/constants.get('robot_radius'))
    # Create map nxm
    map = []
    for i in range(n):
        map.append([])
        for j in range(m):
            map[i].append(0)

    for i in shelf_pos:
        map[i[0]][i[1]] = 1
    for i in charging_pos:
        map[i[0]][i[1]] = 1
    for i in unload_pos:
        map[i[0]][i[1]] = 1
    return map


def create_empty_matrix(map_width, map_length):

    # n = int(map_width/constants.get('robot_radius'))
    #m = int(map_length/constants.get('robot_radius'))
    n = map_width
    m = map_length
    # Create map nxm
    map = []
    for i in range(n):
        map.append([])
        for j in range(m):
            map[i].append(0)
    return map


