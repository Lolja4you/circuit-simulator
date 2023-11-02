import math


class DrawLineUtils:
    def rotate_line(canvas, x1, y1, lenght=100, angle=0, color='white'):
        # the center of the lines is the lower left corner
        angle_rad = -1 * angle * math.pi / 180

        new_x1 = x1
        new_y1 = y1
        new_x2 = lenght
        new_y2 = new_y1


        new_x2 = x1 + lenght * math.cos(angle_rad)
        new_y2 = y1 + lenght * math.sin(angle_rad)

        canvas.create_line(new_x1, new_y1, new_x2, new_y2, width=3, fill=f"{color}")
