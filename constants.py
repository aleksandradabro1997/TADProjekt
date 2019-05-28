from enum import Enum

# Constant values definitions
constants = dict()
constants['map_width'] = 800
constants['map_length'] = 600
constants['max_power'] = 100
constants['robot_color'] = (255, 165, 0)
constants['shelf_color'] = (255, 0, 255)
constants['charging_point_color'] = (0, 128, 0)
constants['unload_point_color'] = (255, 128, 0)
constants['screen_color'] = (255, 255, 255)
constants['robot_base'] = [700, 500]
constants['robot_radius'] = 15


# Statuses definitions
class StatusesRobot(Enum):
    FREE = 0
    BUSY = 1
    CHARGING = 2


class StatusesRack(Enum):
    CAN_BE_MOVED = 0
    CANNOT_BE_MOVED = 1


class StatusesChargingPoint(Enum):
    FREE = 0
    BUSY = 1


def check_if_position_is_valid(x_pos, y_pos):
    if (x_pos < constants.get('map_width') and x_pos > 0
        and y_pos > 0 and y_pos < constants.get('map_length')):
        return True
    else:
        return False


def calculate_charging_time(robot):
    power_lack = constants.get('max_level') - robot.power_left
    if power_lack < 50:
        pass
    else:
        pass
