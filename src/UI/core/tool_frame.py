import tkinter as tk

from src.UI.core.icon import *
from ..screens.table import Table
from ..screens.vector_diagram import VectorDiagram
from ..screens.propertys import Propertys

class ToolFrame(tk.Frame):
    def __init__(self, parent, width, circuit_init):
        self.parent = parent 
        super().__init__(parent, borderwidth=2, relief="solid", width=width * 0.50, height=50, background='#484848')
        self.create_tool_icons()
        self.tool_buttons = {}
        for tool, icon in self.tool_icons.items():
            button = tk.Button(self, text=tool, 
                                command=lambda t=tool: self.select_tool(t, circuit_init),
                                fg='silver', 
                                font=('Arial', 12), 
                                bg='#484848',
                                highlightthickness=0,
                                bd=0
            )
            button.pack(side="left")
            self.tool_buttons[tool] = button
            self.parent.canvas.create_window((30, 30), anchor="nw", window=icon)


    def create_tool_icons(self):
        self.tool_icons = {
            "сформировать отчет": draw_ammeter_icon(self.parent.canvas),
            "софрмировать векторную диаграмму" : draw_ammeter_icon(self.parent.canvas),
            "софрмировать таблицу свойств компонентов" : draw_ammeter_icon(self.parent.canvas),
        }

    def select_tool(self, tool, circuit_init):
        print(f"Selected tool: {tool}")
        if tool == "сформировать отчет":  # Проверьте, выбран ли инструмент "сформировать отчет"
            self.start_table_window(circuit_init)
        elif tool ==  "софрмировать векторную диаграмму":
            self.start_vector_window(circuit_init)
        elif tool ==  "софрмировать таблицу свойств компонентов":
            self.start_propertys_window(circuit_init)

    def start_table_window(self, circuit_init):
        table = Table(circuit_init)
        table.mainloop()

    def start_vector_window(self, circuit_init):
        vector = VectorDiagram(circuit_init)
        vector.mainloop()

    def start_propertys_window(self, circuit_init):
        propertys = Propertys(circuit_init)
        propertys.mainloop()