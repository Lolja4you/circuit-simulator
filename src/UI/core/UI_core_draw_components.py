import math

import tkinter as tk

from src.UI.utils.UI_utils_rotate import rotate_line, spin_rotation, find_angle, find_length


class DrawNode:
    def __init__(
            self, canvas, 
            x: int, y: int, pk:int = 0, 
            color: str = 'white', 
            length: int = 0, 
            angle: int = 0,
            ciruit:object=None
    ):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.selected = False
        self.ciruit = ciruit
        self.pk = pk
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
            self.ciruit.components_matrix_incidence[self.pk]['x'] = self.x
            self.ciruit.components_matrix_incidence[self.pk]['y'] = self.y

    def change_features(self):
        self.ciruit.is_changed = True
        print(self.ciruit.is_changed)

class DrawWire(DrawNode):
    def __init__(
            self, *args, 
            is_node_1=True, 
            is_node_2=True, 
            is_arrow=False, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.x1, self.y1, self.x2, self.y2 = rotate_line(self.x, self.y, angle=self.angle, length=self.length) 
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        vector_21_8_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=21.8+self.angle
        )
        # vector_21_8_degree.draw()

        vector_338_2_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=338.2+self.angle
        )
        # vector_338_2_degree.draw()

        vector_158_2_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=158.2+self.angle
        )
        # vector_158_2_degree.draw()

        vector_201_8_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=201.8+self.angle
        )
        # vector_201_8_degree.draw()

        right_border = self.canvas.create_line(
            vector_21_8_degree.x2,
            vector_21_8_degree.y2,
            vector_338_2_degree.x2,
            vector_338_2_degree.y2, 
            fill=self.color,
            width=3
        )
        right_border

        left_border = self.canvas.create_line(
            vector_158_2_degree.x2,
            vector_158_2_degree.y2,
            vector_201_8_degree.x2,
            vector_201_8_degree.y2, 
            fill=self.color,
            width=3
        )
        left_border

        top_border = self.canvas.create_line(
            vector_158_2_degree.x2,
            vector_158_2_degree.y2,
            vector_21_8_degree.x2,
            vector_21_8_degree.y2, 
            fill=self.color,
            width=3
        )
        top_border

        bottom_border = self.canvas.create_line(
            vector_338_2_degree.x2,
            vector_338_2_degree.y2,
            vector_201_8_degree.x2,
            vector_201_8_degree.y2, 
            fill=self.color,
            width=3
        )
        bottom_border

        self.right_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_21_8_degree.x2+vector_338_2_degree.x2)/2),
            y=round(abs(vector_21_8_degree.y2+vector_338_2_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = self.angle,
            length=50,
            color=self.color,
        )
        self.right_conductor.draw()

        self.left_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_158_2_degree.x2+vector_201_8_degree.x2)/2),
            y=round(abs(vector_158_2_degree.y2+vector_201_8_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = 180+self.angle,
            length=50,
            color=self.color,
        )
        self.left_conductor.draw()
        name = self.ciruit.components_matrix_incidence[self.pk]["name"]
        value = self.ciruit.components_matrix_incidence[self.pk]["resistance"]

        self.vector_text = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=71,
            angle=135+self.angle+180*round(self.angle/180),
        )
        self.vector_text

        self.canvas.create_text(
            self.vector_text.x2, 
            self.vector_text.y2, 
            text=f"{name} {value}Om", 
            font=("Arial", 14), 
            fill='white', 
            angle=self.angle+180*round(self.angle/180), 
            anchor='sw'
        )

    def contains(self, x, y):
        # Получаем координаты вершин прямоугольника после поворота
        vector_21_8_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=21.8+self.angle
        )

        vector_338_2_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=338.2+self.angle
        )

        vector_158_2_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=158.2+self.angle
        )

        vector_201_8_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=54,
            angle=201.8+self.angle
        )
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(vector_338_2_degree.x2, vector_201_8_degree.x2, vector_158_2_degree.x2,  vector_21_8_degree.x2)
        max_x = max(vector_338_2_degree.x2, vector_201_8_degree.x2, vector_158_2_degree.x2,  vector_21_8_degree.x2)
        min_y = min(vector_338_2_degree.y2, vector_201_8_degree.y2, vector_158_2_degree.y2,  vector_21_8_degree.y2)
        max_y = max(vector_338_2_degree.y2, vector_201_8_degree.y2, vector_158_2_degree.y2,  vector_21_8_degree.y2)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False

        
        
    # def select(self):
    #     self.color = '#00CF00'
    #     self.selected = True
    #     print(self.pk)
    #     print(self.__dict__)

    def select(self):
        super().select()
        

    def deselect(self):
        self.color = 'white'
        self.selected = False

    def is_selected(self):
        return self.selected

    def change_features(self):
        super().change_features()
        def check_add_inductor():
            resistance = float(resistance_entry.get())
            if resistance < 1 or resistance > 1000:
                
                tk.messagebox.showerror("Ошибка", "Допустимый диапазон резестивности: 1-1000 (Ом).")
                return

            self.ciruit.components_matrix_incidence[self.pk]['resistance'] = resistance
            tk.messagebox.showinfo("Успех", "резестивность успешно изменена.")
            self.draw()
            root.destroy()

        root = tk.Tk()
        root.title("Изменение данных резестивности")

        resistance_label = tk.Label(root, text="Укажите резестивность:")
        resistance_label.pack()
        resistance_entry = tk.Entry(root)
        resistance_entry.pack()

        add_button = tk.Button(root, text="Изменить резестивность", command=check_add_inductor)
        add_button.pack()

        root.mainloop()
    
class DrawCapacitor(DrawNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def draw(self):
        vector_81_9_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=81.9+self.angle
        )
        # vector_81_9_degree.draw()

        vector_98_1_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=98.1+self.angle
        )
        # vector_98_1_degree.draw()

        vector_261_9_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=261.9+self.angle
        )
        # vector_261_9_degree.draw()

        vector_278_1_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=278.1+self.angle
        )
        # vector_278_1_degree.draw()

        right_lining  = self.canvas.create_line(
            vector_278_1_degree.x2,
            vector_278_1_degree.y2,
            vector_81_9_degree.x2,
            vector_81_9_degree.y2, 
            fill=self.color,
            width=3
        )
        right_lining

        left_lining  = self.canvas.create_line(
            vector_261_9_degree.x2,
            vector_261_9_degree.y2,
            vector_98_1_degree.x2,
            vector_98_1_degree.y2, 
            fill=self.color,
            width=3
        )
        left_lining

        self.right_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_81_9_degree.x2+vector_278_1_degree.x2)/2),
            y=round(abs(vector_81_9_degree.y2+vector_278_1_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = self.angle,
            length=94,
            color=self.color,
        )
        self.right_conductor.draw()

        self.left_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_98_1_degree.x2+vector_261_9_degree.x2)/2),
            y=round(abs(vector_98_1_degree.y2+vector_261_9_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = 180+self.angle,
            length=94,
            color=self.color,
        )
        self.left_conductor.draw()

        name = self.ciruit.components_matrix_incidence[self.pk]["name"]
        value = self.ciruit.components_matrix_incidence[self.pk]["capacitance"]

        self.vector_text = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=71,
            angle=135+self.angle+180*round(self.angle/180),
        )

        self.canvas.create_text(
            self.vector_text.x2, 
            self.vector_text.y2, 
            text=f"{name} {value}F", 
            font=("Arial", 14), 
            fill='white', 
            angle=self.angle+180*round(self.angle/180), 
            anchor='sw'
        )


    def contains(self, x, y):
        vector_81_9_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=81.9+self.angle
        )
        # vector_81_9_degree.draw()

        vector_98_1_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=98.1+self.angle
        )
        # vector_98_1_degree.draw()

        vector_261_9_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=261.9+self.angle
        )
        # vector_261_9_degree.draw()

        vector_278_1_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=41,
            angle=278.1+self.angle
        )
        # vector_278_1_degree.draw()
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(vector_81_9_degree.x2, vector_98_1_degree.x2, vector_261_9_degree.x2, vector_278_1_degree.x2)
        max_x = max(vector_81_9_degree.x2, vector_98_1_degree.x2, vector_261_9_degree.x2, vector_278_1_degree.x2)
        min_y = min(vector_81_9_degree.y2, vector_98_1_degree.y2, vector_261_9_degree.y2, vector_278_1_degree.y2)
        max_y = max(vector_81_9_degree.y2, vector_98_1_degree.y2, vector_261_9_degree.y2, vector_278_1_degree.y2)
        
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
    
    def change_features(self):
        super().change_features()
        def check_add_inductor():
            capacitance = float(resistance_entry.get())
            if capacitance < 1e-3 or  capacitance > 0.005:
                tk.messagebox.showerror("Ошибка", "Допустимый диапазон ёмоксти: 0.05-0.1 (Ф).")
                return

            self.ciruit.components_matrix_incidence[self.pk]['capacitance'] = capacitance
            tk.messagebox.showinfo("Успех", "Конденсатор успешно изменен.")
            self.draw()
            root.destroy()

        root = tk.Tk()
        root.title("Изменение данных ёмкости")

        resistance_label = tk.Label(root, text="Укажите ёмкость:")
        resistance_label.pack()
        resistance_entry = tk.Entry(root)
        resistance_entry.pack()

        add_button = tk.Button(root, text="Изменить ёмкость", command=check_add_inductor)
        add_button.pack()

        root.mainloop()

class DrawSource(DrawNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        length = 35
        vector_45_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=length,
            angle=45+self.angle
        )
        # vector_45_degree.draw()

        vector_135_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=length,
            angle=135+self.angle
        )
        # vector_135_degree.draw()

        vector_225_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=length,
            angle=225+self.angle
        )
        # vector_225_degree.draw()

        vector_315_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=length,
            angle=315+self.angle
        )
        # vector_315_degree.draw()

        body = self.canvas.create_oval(
            self.x - 27, 
            self.y - 27,
            self.x + 27,
            self.y + 27,
            outline=self.color,
            width=3,
        )
        body 
        self.right_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_45_degree.x2+vector_315_degree.x2)/2),
            y=round(abs(vector_45_degree.y2+vector_315_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = self.angle,
            length=75,
            color=self.color
        )
        self.right_conductor.draw()

        self.left_conductor =  DrawWire(
            self.canvas,
            x=round(abs(vector_135_degree.x2+vector_225_degree.x2)/2),
            y=round(abs(vector_135_degree.y2+vector_225_degree.y2)/2),
            is_arrow=False,
            is_node_1=False,
            is_node_2=True,
            angle = 180+self.angle,
            length=75,
            color=self.color
        )
        self.left_conductor.draw()

        arrow = DrawWire(
            self.canvas,
            x=round(abs(vector_135_degree.x2+vector_225_degree.x2)/2),
            y=round(abs(vector_135_degree.y2+vector_225_degree.y2)/2),
            is_arrow=True,
            is_node_1=False,
            is_node_2=False,
            angle = self.angle,
            length=54,
            color=self.color
        )
        arrow.draw()

        name = self.ciruit.components_matrix_incidence[self.pk]["name"]
        value = abs(float(self.ciruit.components_matrix_incidence[self.pk]["amplitude"]))
        frequency = self.ciruit.components_matrix_incidence[self.pk]["frequency"]

        self.vector_text = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=71,
            angle=135+self.angle+180*round(self.angle/180),
        )

        self.canvas.create_text(
            self.vector_text.x2, 
            self.vector_text.y2, 
            text=f"{name} {abs(value)}V {frequency}Hz", 
            font=("Arial", 14), 
            fill='white', 
            angle=self.angle+180*round(self.angle/180), 
            anchor='sw'
        )
    def contains(self, x, y):
        vector_45_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=27,
            angle=45+self.angle
        )
        # vector_45_degree.draw()

        vector_135_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=27,
            angle=135+self.angle
        )
        # vector_135_degree.draw()

        vector_225_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=27,
            angle=225+self.angle
        )
        # vector_225_degree.draw()

        vector_315_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=27,
            angle=315+self.angle
        )
        # vector_315_degree.draw()
        
        # Находим минимальные и максимальные координаты по осям X и Y
        min_x = min(vector_45_degree.x2, vector_135_degree.x2, vector_225_degree.x2, vector_315_degree.x2)
        max_x = max(vector_45_degree.x2, vector_135_degree.x2, vector_225_degree.x2, vector_315_degree.x2)
        min_y = min(vector_45_degree.y2, vector_135_degree.y2, vector_225_degree.y2, vector_315_degree.y2)
        max_y = max(vector_45_degree.y2, vector_135_degree.y2, vector_225_degree.y2, vector_315_degree.y2)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False
        
    def change_features(self):
        super().change_features()
        def check_add_inductor():
            capacitance = float(resistance_entry.get())
            frequency = float(frequency_entry.get())
            if abs(capacitance) > 12:
                tk.messagebox.showerror("Ошибка", "Допустимый диапазон амплитуды: -12 до 12.")
                return
            if frequency < 40 or frequency > 70:
                tk.messagebox.showerror("Ошибка", "Допустимый диапазон частоты: 40 до 70.")
                return
            
            self.ciruit.components_matrix_incidence[self.pk]['amplitude'] = capacitance
            self.ciruit.components_matrix_incidence[self.pk]['frequency'] = frequency
            tk.messagebox.showinfo("Успех", "Source is changed.")

            self.draw()
            root.destroy()

        root = tk.Tk()
        root.title("Change Source")

        frequency_label = tk.Label(root, text="Укажите частоту:")
        frequency_label.pack()
        frequency_entry = tk.Entry(root)
        frequency_entry.pack()

        resistance_label = tk.Label(root, text="Укажите амплитуду:")
        resistance_label.pack()
        resistance_entry = tk.Entry(root)
        resistance_entry.pack()

        add_button = tk.Button(root, text="Change source", command=check_add_inductor)
        add_button.pack()

        root.mainloop()

class DrawInductor(DrawNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        vector_30_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=30+self.angle
            )
        # vector_30_degree.draw()

        vector_120_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=150+self.angle
        )
        # vector_120_degree.draw()

        vector_210_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=210+self.angle
        )
        # vector_210_degree.draw()

        vector_300_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=-30+self.angle
        )
        # vector_300_degree.draw()

        self.canvas.create_arc(self.x-50, self.y-11, self.x-25, self.y+14,        start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x-25, self.y-11, self.x, self.y+14,     start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x, self.y-11, self.x+25, self.y+14,     start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        self.canvas.create_arc(self.x+25, self.y-11, self.x+50, self.y+14,    start=0,  extent=180, outline=self.color, width=3, style=tk.ARC)
        
        self.left_conductor = DrawWire(
            self.canvas,
            self.x-50,
            self.y,
            length=50, angle=180,
            is_arrow=False , 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )
        self.left_conductor.draw()
        self.right_conductor = DrawWire(
            self.canvas,
            self.x+50,
            self.y,
            length=50, angle=0,
            is_arrow=False, 
            is_node_1=False,
            is_node_2=True,
            color=self.color,
        )
        self.right_conductor.draw()

        name = self.ciruit.components_matrix_incidence[self.pk]["name"]
        value = self.ciruit.components_matrix_incidence[self.pk]["inductance"]
        self.vector_text = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=154+self.angle+180*round(self.angle/180),
        )

        self.canvas.create_text(
            self.vector_text.x2, 
            self.vector_text.y2, 
            text=f"{name} {value}H", 
            font=("Arial", 14), 
            fill='white', 
            angle=self.angle+180*round(self.angle/180), 
            anchor='sw'
        )


    def contains(self, x, y):
        vector_30_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=30+self.angle
            )
        # vector_30_degree.draw()

        vector_120_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=150+self.angle
        )
        # vector_120_degree.draw()

        vector_210_degree =  DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=210+self.angle
        )
        # vector_210_degree.draw()

        vector_300_degree = DrawWire(
            self.canvas, 
            is_node_1=False,
            is_node_2=False,
            x=self.x,
            y=self.y,
            length=56,
            angle=-30+self.angle
        )
        # vector_300_degree.draw()

        min_x = min(vector_30_degree.x2, vector_120_degree.x2, vector_210_degree.x2, vector_300_degree.x2)
        max_x = max(vector_30_degree.x2, vector_120_degree.x2, vector_210_degree.x2, vector_300_degree.x2)
        min_y = min(vector_30_degree.y2, vector_120_degree.y2, vector_210_degree.y2, vector_300_degree.y2)
        max_y = max(vector_30_degree.y2, vector_120_degree.y2, vector_210_degree.y2, vector_300_degree.y2)
        
        # Проверяем, находятся ли переданные координаты внутри прямоугольника
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
        else:
            return False
        
    def change_features(self):
        super().change_features()
        def check_add_inductor():
            capacitance = float(resistance_entry.get())
            if capacitance < 1e-3 or  capacitance > 0.005:
                tk.messagebox.showerror("Ошибка", "Допустимый диапазон индуктивности: 0.05-0.1 (Ф).")
                return

            self.ciruit.components_matrix_incidence[self.pk]['capacitance'] = capacitance
            tk.messagebox.showinfo("Успех", "индуктивность успешно изменена.")
            self.draw()
            root.destroy()

        root = tk.Tk()
        root.title("Изменение данных индуктивности")

        resistance_label = tk.Label(root, text="Укажите индуктивность:")
        resistance_label.pack()
        resistance_entry = tk.Entry(root)
        resistance_entry.pack()

        add_button = tk.Button(root, text="Изменить индуктивность", command=check_add_inductor)
        add_button.pack()

        root.mainloop()