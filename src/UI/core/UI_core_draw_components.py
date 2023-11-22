import tkinter as tk

from src.UI.utils.UI_utils_rotate import rotate_line, spin_rotation, find_angle, find_length

class DrawNode:
    def __init__(self, canvas, x: int, y: int, color: str = 'white', length: int = 0, angle: int = 0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.selected = False
        self.__radius = 10
        self.__width = 3

    def select(self):
        self.color = '#00CF00'
        self.selected = True

    def deselect(self):
        self.color = 'white'
        self.selected = False
    
    def contains(self, x, y):
        top_left_x = self.x - (self.__radius/2)
        top_left_y = self.y - (self.__radius/2)
        bottom_right_x = self.x + (self.__radius/2)
        bottom_right_y = self.y + (self.__radius/2)
        top_left_x, top_left_y, bottom_right_x, bottom_right_y= spin_rotation(top_left_x,top_left_y,bottom_right_x,bottom_right_y,length=self.length,angle=self.angle,)
        if top_left_x <= x <= bottom_right_x and top_left_y <= y <= bottom_right_y:
            return True
        else:
            return False

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
    
    def drag(self, dx, dy):
        if self.selected:
            dx = dx - self.x
            dy = dy - self.y
            self.x += dx
            self.y += dy

class DrawWire(DrawNode):
    def __init__(self, canvas, x, y, color='white', length=0, angle=0, is_node_1 = True, is_node_2 = True, is_arrow=False):
        super().__init__(canvas, x, y, color, length, angle)
        self.x1,self.y1,self.x2,self.y2 = rotate_line(self.x, self.y, angle=self.angle, length=self.length) 
        self.is_node_1 = is_node_1
        self.is_node_2 = is_node_2
        self.is_arrow = is_arrow

    def draw(self):
        if not self.is_arrow:
            self.canvas.create_line(
                rotate_line(
                    self.x, self.y, angle=self.angle, length=self.length
                ), 
                width=self._DrawNode__width, 
                fill=self.color
            )
        else:
            self.canvas.create_line(
                rotate_line(
                    self.x, self.y, angle=self.angle, length=self.length
                ), 
                width=self._DrawNode__width, 
                fill=self.color,
                arrow=tk.LAST
            )
        if not self.is_node_1:...
        else: 
            node_1 = DrawNode(self.canvas, self.x, self.y, angle=self.angle, color=self.color)
            node_1.draw()
        if not self.is_node_2:...
        else:
            node_2 = DrawNode(self.canvas, self.x, self.y, length=self.length, angle=self.angle, color=self.color,
            )
            node_2.draw()

    def contains(self, x, y):
        x1, y1, x2, y2 = rotate_line(self.x, self.y, angle=self.angle, length=self.length)
        m = round(-1 * find_angle(x1, y1, x, y),0)
        length = find_length(x1,y1,x,y)
        if abs(m  - self.angle) <=3 and self.length>=length: 
            return True
        else:
            return False

    def select(self):
        self.color = '#00CF00'
        self.selected = True

    def deselect(self):
        self.color = 'white'
        self.selected = False

    def is_selected(self):
        return self.selected


class DrawResisrtor(DrawNode):
    def __init__(self, canvas, x, y, color='white', length=0, angle=0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):
        left_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y,
            length=40, angle=90+self.angle, 
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        bottom_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y, 
            length=100, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )

        top_border = DrawWire(
            self.canvas, 
            left_border.x2, left_border.y2, 
            length=100, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        right_border = DrawWire(
            self.canvas, 
            bottom_border.x2, 
            bottom_border.y2, 
            length=40, angle=90+self.angle, 
            is_node_1=False, is_node_2=False,
            color=self.color
        )
        
        left_border.draw()
        bottom_border.draw()

        top_border.draw()
        right_border.draw()

        left_conductor = DrawWire(
            self.canvas, 
            left_border.x1+(left_border.x2-left_border.x1)/2, 
            left_border.y1+(left_border.y2-left_border.y1)/2, 
            length=-50, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        left_conductor.draw()

        right_conductor = DrawWire(
            self.canvas, 
            right_border.x1+(right_border.x2-right_border.x1)/2, 
            right_border.y1+(right_border.y2-right_border.y1)/2, 
            length=50, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        right_conductor.draw()

    def contains(self, x, y):
        # Получаем координаты вершин прямоугольника после поворота
        x1_bottom, y1_bottom, x2_bottom, y2_bottom = rotate_line(self.x, self.y, angle=self.angle, length=100)
        x1_up, y1_up, x2_up, y2_up = rotate_line(x2_bottom, y2_bottom, angle=self.angle + 90, length=40)
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(x1_bottom, x2_bottom, x1_up, x2_up)
        max_x = max(x1_bottom, x2_bottom, x1_up, x2_up)
        min_y = min(y1_bottom, y2_bottom, y1_up, y2_up)
        max_y = max(y1_bottom, y2_bottom, y1_up, y2_up)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False

        
        
    def select(self):
        self.color = '#00CF00'
        self.selected = True

    def deselect(self):
        self.color = 'white'
        self.selected = False

    def is_selected(self):
        return self.selected
    
class DrawCapacitor(DrawNode):
    def __init__(self, canvas, x: int, y: int, angle: int, color: str = 'white', length: int = 0, ):
        super().__init__(canvas, x, y, color=color, length=length, angle=angle)
    
    def draw(self):
        left_lining = DrawWire(
            self.canvas,
            self.x, self.y,
            length=80, angle=90+self.angle,
            is_arrow=False, 
            is_node_1=False,
            is_node_2=False,
            color=self.color
        )        
        
        bottom_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y, 
            length=14, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )

        right_lining =DrawWire(
            self.canvas,
            bottom_border.x2, 
            bottom_border.y2, 
            length=80, angle=90+self.angle,
            is_arrow=False, 
            is_node_1=False,
            is_node_2=False,
            color=self.color
        )
        left_lining.draw()
        right_lining.draw()

        left_conductor = DrawWire(
            self.canvas, 
            left_lining.x1+(left_lining.x2-left_lining.x1)/2, 
            left_lining.y1+(left_lining.y2-left_lining.y1)/2, 
            length=-94, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        left_conductor.draw()

        right_conductor = DrawWire(
            self.canvas, 
            right_lining.x1+(right_lining.x2-right_lining.x1)/2, 
            right_lining.y1+(right_lining.y2-right_lining.y1)/2, 
            length=94, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        right_conductor.draw()


    def contains(self, x, y):
        x1_bottom, y1_bottom, x2_bottom, y2_bottom = rotate_line(self.x, self.y, angle=self.angle, length=14)
        x1_up, y1_up, x2_up, y2_up = rotate_line(x2_bottom, y2_bottom, angle=self.angle + 90, length=80)
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(x1_bottom, x2_bottom, x1_up, x2_up)
        max_x = max(x1_bottom, x2_bottom, x1_up, x2_up)
        min_y = min(y1_bottom, y2_bottom, y1_up, y2_up)
        max_y = max(y1_bottom, y2_bottom, y1_up, y2_up)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        # print(min_x,max_x,min_y,max_y)
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False
    
    def select(self):
        return super().select()
    
    def deselect(self):
        self.color = 'white'
        self.selected = False

    def is_selected(self):
        return self.selected
    
class DrawSource(DrawNode):
    def __init__(self, canvas, x: int, y: int, color: str = 'white', length: int = 40, angle: int = 0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):
        left_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y,
            length=80, angle=90+self.angle, 
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        bottom_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y, 
            length=80, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        right_border = DrawWire(
            self.canvas, 
            bottom_border.x2, 
            bottom_border.y2, 
            length=80, angle=90+self.angle, 
            is_node_1=False, is_node_2=False,
            color=self.color
        )
        # left_border.draw()
        # right_border.draw()
        # bottom_border.draw()
        self.canvas.create_oval(
            left_border.x1, left_border.y1, right_border.x2, right_border.y2, outline=self.color, width=3 
        )
        draw_arrow = DrawWire(
            self.canvas,
            bottom_border.x1 + (bottom_border.x2-bottom_border.x1)/2, 
            left_border.y1+(right_border.y1-left_border.y1)/2, 
            length=self.length*2, angle=90+self.angle,
            is_arrow=True, 
            is_node_1=False,
            is_node_2=False,
            color=self.color
        )

        draw_arrow.draw()

        left_conductor = DrawWire(
            self.canvas,
            draw_arrow.x2,
            draw_arrow.y2,
            length=60, angle=90+self.angle,
            is_arrow=False , 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )

        right_conductor = DrawWire(
            self.canvas,
            draw_arrow.x1,
            draw_arrow.y1,
            length=60, angle=-90+self.angle,
            is_arrow=False, 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )

        left_conductor.draw()
        right_conductor.draw()

    def contains(self, x, y):
        # Получаем координаты вершин прямоугольника после поворота
        x1_bottom, y1_bottom, x2_bottom, y2_bottom = rotate_line(self.x, self.y, angle=self.angle, length=80)
        x1_up, y1_up, x2_up, y2_up = rotate_line(x2_bottom, y2_bottom, angle=self.angle + 90, length=80)
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(x1_bottom, x2_bottom, x1_up, x2_up)
        max_x = max(x1_bottom, x2_bottom, x1_up, x2_up)
        min_y = min(y1_bottom, y2_bottom, y1_up, y2_up)
        max_y = max(y1_bottom, y2_bottom, y1_up, y2_up)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False
        


class DrawInductor(DrawNode):
    def __init__(self, canvas, x: int, y: int, color: str = 'white', length: int = 0, angle: int = 0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):


        self.canvas.create_arc(self.x, self.y, self.x+25, self.y+25,        start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x+25, self.y, self.x+50, self.y+25,     start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x+50, self.y, self.x+75, self.y+25,     start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x+75, self.y, self.x+100, self.y+25,    start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        
        left_conductor = DrawWire(
            self.canvas,
            self.x,
            self.y+11,
            length=50, angle=180,
            is_arrow=False , 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )
        left_conductor.draw()
        right_conductor = DrawWire(
            self.canvas,
            self.x+100,
            self.y+11,
            length=50, angle=0,
            is_arrow=False, 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )
        right_conductor.draw()
    def contains(self, x, y):
        # Получаем координаты вершин прямоугольника после поворота
        x1_bottom, y1_bottom, x2_bottom, y2_bottom = rotate_line(self.x, self.y, angle=0, length=100)
        x1_up, y1_up, x2_up, y2_up = rotate_line(self.x, self.y, angle=90, length=10)
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(x1_bottom, x2_bottom, x1_up, x2_up)
        max_x = max(x1_bottom, x2_bottom, x1_up, x2_up)
        min_y = min(y1_bottom, y2_bottom, y1_up, y2_up)
        max_y = max(y1_bottom, y2_bottom, y1_up, y2_up)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False
        
