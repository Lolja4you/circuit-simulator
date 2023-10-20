import tkinter as tk

from src.UI.core.icon import *

class ToolFrame(tk.Frame):
    def __init__(self, parent, width):
        self.parent = parent 
        super().__init__(parent, borderwidth=2, relief="solid", width=width * 0.50, height=50, background='#484848')
        self.create_tool_icons()
        self.tool_buttons = {}
        for tool, icon in self.tool_icons.items():
            button = tk.Button(self, text=tool, 
                                command=lambda t=tool: self.select_tool(t),
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
            "source": draw_source_icon(self.parent.canvas),
            "node": draw_node_icon(self.parent.canvas),
            "resistor": draw_resistor_icon(self.parent.canvas),
            "capacitor": draw_capacitor_icon(self.parent.canvas),
            "inductor": draw_inductor_icon(self.parent.canvas),
            "voltmeter": draw_voltmeter_icon(self.parent.canvas),
            "ammeter": draw_ammeter_icon(self.parent.canvas)
        }

    def select_tool(self, tool):
        print(f"Selected tool: {tool}")
