import math


def rotate_line(x1, y1, angle, length) -> tuple:
    # the center of the lines is the lower left corner
    angle_rad = -1 * angle * math.pi / 180

    new_x1 = x1
    new_y1 = y1
    new_x2 = length
    new_y2 = new_y1

    new_x2 = x1 + length * math.cos(angle_rad)
    new_y2 = y1 + length * math.sin(angle_rad)

    return new_x1, new_y1, new_x2, new_y2

def spin_rotation(x1, y1, x2, y2, angle, length=0):
    angle_rad = -1 * angle * math.pi / 180

    x1 = x1 + length * math.cos(angle_rad)
    y1 = y1 + length * math.sin(angle_rad)
    x2 = x2 + length * math.cos(angle_rad)
    y2 = y2 + length * math.sin(angle_rad)

    return x1,y1,x2,y2


def find_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)
    return math.degrees(angle)


def find_length(x1,y1,x2,y2):
    length = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return length