from src.UI.utils.UI_utils_rotate import rotate_line, spin_rotation


class DrawNode:
    def __init__(self, canvas, x: int, y: int, color: str = 'silver', length: int = 0, angle: int = 0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.__radius = 10
        self.__width = 3

    def draw(self):
        top_left_x = self.x - (self.__radius/2)
        top_left_y = self.y - (self.__radius/2)
        bottom_right_x = self.x + (self.__radius/2)
        bottom_right_y = self.y + (self.__radius/2)

        self.canvas.create_oval(
            spin_rotation(
                top_left_x, top_left_y, 
                bottom_right_x, bottom_right_y,
                length=self.length,
                angle=self.angle,
            ),
            fill=self.color,
        )

    def move(self, dx=None, dy=None):
        self.x += dx
        self.y += dy
        self.draw()

class DrawWire(DrawNode):
    def __init__(self, canvas, x, y, color='white', length=0, angle=0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):
        self.canvas.create_line(
            rotate_line(
                self.x, self.y, angle=self.angle, length=self.length
            ), 
            width=self._DrawNode__width, 
            fill=self.color
        )
        node_1 = DrawNode(self.canvas, self.x, self.y, angle=self.angle)
        node_1.draw()
        node_2 = DrawNode(
            self.canvas, self.x, self.y,
            length=self.length, angle=self.angle
        )
        node_2.draw()

    def move(self, dx, dy):
        super().move(dx, dy)


class DrawResisrtor(DrawNode):
    def __init__(self, canvas, x, y, color='white', length=0, angle=0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):
        #bottom-left 
        left_border = DrawWire(self.canvas, x=self.x, y=self.y, length=40, angle=90+self.angle, color=self.color)
        bottom_border = DrawWire(self.canvas, x=self.x, y=self.y, length=100, angle=self.angle, color=self.color)
        #top right
        top_border = DrawWire(self.canvas, x=self.x, y=self.y, length=100, angle=self.angle, color=self.color)
        left_border.draw()
        # right_border.draw()
        top_border.draw()
        bottom_border.draw()
    
    def move(self, dx, dy):
        super().move(dx, dy)
    