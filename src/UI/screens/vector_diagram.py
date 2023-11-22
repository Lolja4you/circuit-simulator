import tkinter as tk
from tkinter import ttk
import math
from ..core.UI_core_draw_components import DrawWire
from src.UI.utils.UI_utils_rotate import find_angle

class VectorDiagram(tk.Tk):
    def __init__(self, circuit_init):
        super().__init__()
        self.circuit_init = circuit_init
        self.x = self.winfo_screenwidth()
        self.y = self.winfo_screenheight()
        self.title("test_1 - vectors diagram")
        self.configure(bg='#030B15')

        self.resisotr: object
        self.capacitor: object
        self.induction: object
        self.voltage: object

        width = int(round(self.x/1.5, 0))
        height = int(round(self.y/1.1, 0))
        print(circuit_init.result)

        x_position = -10
        y_position = 0
        self.geometry(f"{self.x}x{self.y}+{x_position}+{y_position}")

        self.canvas = tk.Canvas(self, width=self.x, height=self.y, bg='#030B15') ##fff9f7
        self.canvas.pack()

        scale_x = DrawWire(self.canvas, 50, 650, color='white', length=100, angle=0, is_node_1=False, is_node_2=False, is_arrow=False)
        scale_x.draw()
        scale_y = DrawWire(self.canvas, 50, 650, color='white', length=100, angle=90, is_node_1=False, is_node_2=False, is_arrow=False)
        scale_y.draw()

        x = DrawWire(self.canvas, 400, 400, color='white', length=700, angle=0, is_node_1=False, is_node_2=False, is_arrow=True)
        x.draw()
        y = DrawWire(self.canvas, 400, 400, color='white', length=380, angle=90, is_node_1=False, is_node_2=False, is_arrow=True)
        y.draw()

        x2 = DrawWire(self.canvas, 400, 400, color='white', length=75, angle=180, is_node_1=False, is_node_2=False, is_arrow=False)
        x2.draw()
        y2 = DrawWire(self.canvas, 400, 400, color='white', length=75, angle=-90, is_node_1=False, is_node_2=False, is_arrow=False)
        y2.draw()
        queue = circuit_init.result.copy()
        def draw_vector(queue):
            for component in queue:
                try:
                    if component[0] == 'R1':
                        self.resistor = DrawWire(self.canvas, x.x1, y.y1, color='red', length=component[1]*10, angle=0, is_node_1=False, is_node_2=False, is_arrow=True)
                        self.resistor.draw()
                    elif component[0] == 'C2':
                        self.capacitor = DrawWire(self.canvas, self.induction.x2-5, self.induction.y2, color='green', length=component[1]*1000, angle=-90, is_node_1=False, is_node_2=False, is_arrow=True)
                        self.capacitor.draw()
                    elif component[0] == 'L3':
                        self.induction = DrawWire(self.canvas, self.resistor.x2, self.resistor.y2, color='blue', length=component[1]*1000, angle=90, is_node_1=False, is_node_2=False, is_arrow=True)
                        self.induction.draw()
                    elif component[0] == 'E4':
                        length = math.sqrt((x.x1-self.capacitor.x2+5)**2+(y.y1-self.capacitor.y2)**2)
                        self.voltage = DrawWire(self.canvas, 400, 400, color='yellow', length=length, angle=-1*find_angle(400, 400, self.capacitor.x2, self.capacitor.y2), is_node_1=False, is_node_2=False, is_arrow=True)
                        self.voltage.draw()
                    queue.remove(component)
                    print(queue)
                except UnboundLocalError:...
        while True:
            if len(queue) !=0:
                draw_vector(queue)
            else:
                break
        # Axis labels
        self.canvas.create_text(x.x1 + 30, x.y1 + 20, text="X-Axis", fill="white", font=("Arial", 12))
        self.canvas.create_text(y.x1 - 25, y.y1 - 30, text="Y-Axis", fill="white", font=("Arial", 12))

        # Легенда
        legend = ttk.Label(self, text="Legend", background='#030B15', foreground='white', font=("Arial", 12))
        legend.place(x=10, y=10)

        resistor_legend = ttk.Label(self, text="Resistor", background='#030B15', foreground='red', font=("Arial", 10))
        resistor_legend.place(x=20, y=40)

        induction_legend = ttk.Label(self, text="Induction", background='#030B15', foreground='blue', font=("Arial", 10))
        induction_legend.place(x=20, y=60)

        capacitor_legend = ttk.Label(self, text="Capacitor", background='#030B15', foreground='green', font=("Arial", 10))
        capacitor_legend.place(x=20, y=80)

        voltage_legend = ttk.Label(self, text="Voltage", background='#030B15', foreground='yellow', font=("Arial", 10))
        voltage_legend.place(x=20, y=100)

        self.canvas.create_text(x.x1 + 30, x.y1 + 20, text="X-Axis", fill="white", font=("Arial", 12))
        self.canvas.create_text(y.x1 - 25, y.y1 - 30, text="Y-Axis", fill="white", font=("Arial", 12))
        self.canvas.create_text(390, 410, text="0", fill="white", font=("Arial", 12))
        self.canvas.create_text(scale_x.x1+abs(scale_x.x1-scale_x.x2)/2, scale_x.y1 - 10, text="10px", fill="white", font=("Arial", 10))
        self.canvas.create_text(scale_y.x1-10, scale_y.y1-abs(scale_y.y1-scale_y.y2)/2, text="1000px", fill="white", font=("Arial", 10), angle=90)
        self.canvas.create_text(scale_x.x1+abs(scale_x.x1-scale_x.x2)/2, scale_x.y1 + 10, text="scale/масштаб", fill="white", font=("Arial", 10))