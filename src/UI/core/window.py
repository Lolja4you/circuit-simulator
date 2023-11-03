import tkinter as tk
from src.UI.core.tool_frame import ToolFrame
from .UI_core_components_processing import components_drawer

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.x = self.winfo_screenwidth()
        self.y = self.winfo_screenheight()
        self.title("test_1 - САПР")

        self.geometry(f"{self.x}x{self.y}")

        self.cam_velocity = 10

        self.canvas = tk.Canvas(self, width=self.x, height=self.y, bg="#484848") ##fff9f7
        self.canvas.pack()

        self.canvas.bind("<Motion>", self.update_cursor_position)
        self.bind("<KeyPress>", self.move_canvas)
        self.canvas.bind("<ButtonPress-2>", self.start_drag)
        self.canvas.bind("<B2-Motion>", self.drag_canvas)

        self.cursor_position_x = tk.StringVar()
        self.cursor_position_y = tk.StringVar()

        '''
        cursor position
        '''
        self.cursor_position_label = tk.Label(self, textvariable=self.cursor_position_x)
        self.cursor_position_label.place(x=10, y=self.y-120)

        self.cursor_position_label2 = tk.Label(self, textvariable=self.cursor_position_y)
        self.cursor_position_label2.place(x=10, y=self.y-100)

        '''
        tool frame
        '''
        self.tool_frame = ToolFrame(self, self.x)
        self.tool_frame.place(x=self.x - (self.x*1) + 10, y=10)

        self.canvas.focus_set()

        self.workspace_width = self.x
        self.workspace_height = self.y
        self.quadrant_size = 200
        self.subsquare_size = self.quadrant_size // 4

        self.x_offset = 0
        self.y_offset = 0

        self.draw_subsquare()
        self.draw_subsquare(wrapped=False)
        self.draw_visible_area()
        self.draw_visible_area(wrapped=True)
        
        '''
        initial drawing components
        '''
        self.node = components_drawer(self.canvas)
        for components in self.node:
            components.draw()
    def draw_visible_area(self, wrapped=False):
        for x in range(int(self.x_offset / self.quadrant_size), int((self.x_offset + self.workspace_width) / self.quadrant_size) + 1):
            for y in range(int(self.y_offset / self.quadrant_size), int((self.y_offset + self.workspace_height) / self.quadrant_size) + 1):
                x1 = x * self.quadrant_size - self.x_offset
                y1 = y * self.quadrant_size - self.y_offset
                x2 = x1 - self.quadrant_size if wrapped else x1 + self.quadrant_size
                y2 = y1 - self.quadrant_size if wrapped else y1 + self.quadrant_size

                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#6fc5db", width=2)

    def draw_subsquare(self, wrapped=False):
        for x in range(int(self.x_offset / self.subsquare_size), int((self.x_offset + self.workspace_width) / self.subsquare_size) + 1):
            for y in range(int(self.y_offset / self.subsquare_size), int((self.y_offset + self.workspace_height) / self.subsquare_size) + 1):
                x1 = x * self.subsquare_size - self.x_offset 
                y1 = y * self.subsquare_size - self.y_offset
                x2 = x1 - self.subsquare_size if wrapped else x1 + self.subsquare_size
                y2 = y1 - self.subsquare_size if wrapped else y1 + self.subsquare_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#888888") #cfcfcf

    def move_canvas(self, event):
        dx, dy = 0, 0

        match event.keysym:
            case 'Up': 
                self.y_offset -= self.cam_velocity
                dy = self.cam_velocity
            case 'Down':
                self.y_offset += self.cam_velocity
                dy = -self.cam_velocity
            case 'Left':
                self.x_offset -= self.cam_velocity
                dx = self.cam_velocity
            case 'Right':
                self.x_offset += self.cam_velocity
                dx = -self.cam_velocity

        self.canvas.delete("all")
        self.draw_subsquare()
        self.draw_subsquare(wrapped=True)
        self.draw_visible_area()
        self.draw_visible_area(wrapped=True)

        self.update_cursor_position(event)

        for components in self.node:
            components.move(dx, dy)

    def start_drag(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def drag_canvas(self, event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y

        self.x_offset -= dx
        self.y_offset -= dy

        self.canvas.delete("all")
        self.draw_subsquare()
        self.draw_subsquare(wrapped=True)
        self.draw_visible_area()
        self.draw_visible_area(wrapped=True)

        self.last_x = event.x
        self.last_y = event.y

        for components in self.node:
            components.move(dx, dy)


    def update_cursor_position(self, event):
        self.cursor_position_x.set(f"X: {event.x+self.x_offset}")
        self.cursor_position_y.set(f"Y: {event.y+self.y_offset}")
