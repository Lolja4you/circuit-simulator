import json

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from src.UI.core.icon import *

from ..screens.table import Table
from ..screens.vector_diagram import VectorDiagram

from ..utils.UI_utils_buttons import DropdownButton


class ToolFrame(tk.Frame):
    def __init__(self, parent, width, circuit_init):
        self.parent = parent 
        self.circuit_init = circuit_init
        super().__init__(parent, borderwidth=2, relief="solid", width=width * 0.50, height=50, background='#484848')
        
        self.app_list = [
            DropdownButton(self, text='file', button_commands=[
                self.init_save,
                self.init_open,
            ]),
            DropdownButton(self, text='report', button_commands=[self.init_calc_report_screen, self.init_vector_report_screen]),
            DropdownButton(self, text='draw', button_commands=[
                self.init_draw_source,
                self.init_draw_resistor,
                self.init_draw_capacitor,
                self.init_draw_inductor,
            ]),

        ]
        for i, button in enumerate(self.app_list):
            button.column = i
            button.grid(row=0, column=i, sticky="nsew")

    def init_calc_report_screen(self):
        """calc report"""        
        table = Table(self.circuit_init)
        if table.is_init:
            table.mainloop()

    def init_vector_report_screen(self):
        """vector diagram"""
        vector = VectorDiagram(self.circuit_init)
        if vector.is_init:
            vector.mainloop()

    def init_draw_source(self):
        """source"""
        from src.logic.add_source import UI_input_source_data
        UI_input_source_data(circuit=self.circuit_init, parent=self.parent)

    def init_draw_resistor(self):
        """resistor"""
        from src.logic.add_resistors import UI_input_resistor_data
        UI_input_resistor_data(circuit=self.circuit_init, parent=self.parent)


    def init_draw_capacitor(self):
        """capacitor"""
        from src.logic.add_capacitor import UI_input_capacitor_data 
        UI_input_capacitor_data(circuit=self.circuit_init, parent=self.parent)

    def init_draw_inductor(self):
        """inductor"""
        from src.logic.add_inductor import UI_input_inductor_data 
        UI_input_inductor_data(circuit=self.circuit_init, parent=self.parent)

    def init_save(self):
        """save"""
        from src.action_event.action_files.save_circuit import save_circuit
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if file_path:
            with open(file_path, 'w') as file:
                serializer_data = {}
                serializer_data['components'] = self.circuit_init.components_matrix_incidence
                serializer_data['connections'] = self.circuit_init.adjacency_dict
                json.dump(serializer_data, file)
            messagebox.showinfo("Успех", f"Файл успешно сохранен {file_path}")    
            print(f"Файл успешно сохранен {file_path}")
        else:
            messagebox.showerror("Ошибка", "Отменено сохранение файла.")
            print("Отменено сохранение файла.")

    def init_open(self):
        """open"""
        file_path = filedialog.askopenfilename(defaultextension=".json")
        if file_path:
            with open(file_path) as json_file:
                open_dict = json.load(json_file)
                for key, value in open_dict['components'].items():
                    new_key = int(key)
                    self.circuit_init.components_matrix_incidence[new_key] = value
                for key, value in open_dict['connections'].items():
                    new_key = int(key)
                    self.circuit_init.components_matrix_adjacency[new_key] = value
                json_file.close()
            messagebox.showinfo("Успех", f"Файл успешно открыт {file_path}")    
            print(f"Файл успешно открыт {file_path}")
            self.parent.re_draw()
        else:
            messagebox.showerror("Ошибка", "Невозможно открыть файл.")
            print("Невозможно открыть файл.")