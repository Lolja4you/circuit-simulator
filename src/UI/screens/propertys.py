import tkinter as tk
from tkinter import ttk

class Propertys(tk.Tk):
    def __init__(self, circuit_init):
        super().__init__()
        self.circuit_init = circuit_init
        self.x = self.winfo_screenwidth()
        self.y = self.winfo_screenheight()
        self.title("test_1 - property table") 
        self.configure(bg='#030B15')

        width = int(round(self.x/1.5, 0))
        height = int(round(self.y/1.1, 0))

        x_position = -10
        y_position = 0
        self.geometry(f"{width}x{height}+{x_position}+{y_position}")

        # Создаем надпись "Свойства компонентов" в жирном шрифте
        label = tk.Label(self, text="Свойства компонентов", font=("Arial", 16, "bold"), bg='#030B15', fg='white')
        label.pack()

        # Создаем текстовое поле для вывода словаря
        self.text = tk.Text(self, font=("Arial", 13), bg='#030B15', fg='white')
        self.text.pack(expand=True, fill=tk.BOTH)

        # Добавляем данные из словаря в текстовое поле
        components_dict = self.circuit_init.components_matrix_incidence
        components_dict = {int(key): value for key, value in components_dict.items()} 
        label = tk.Label(self, text="Последовательность компонентов", font=("Arial", 16, "bold"), bg='#2B2B2B', fg='white')
        label.pack()

        connection_dict = self.circuit_init.components_matrix_adjacency
        connection_dict = {int(key): value for key, value in connection_dict.items()} 
        for index, component in components_dict.items():
            self.text.insert(tk.END, f"{index}: {component}\n")
        for index, component in enumerate(components_dict, start=1):
            self.text.insert(tk.END, f"Connections: {connection_dict.get(component['node_pk'], [])}\n")

        # Изменяем шрифт текстового поля
        self.text.configure(font=("Arial", 12, "normal"))

        # Изменяем цвет текстового поля
        self.text.configure(bg='#2B2B2B', fg='white')

        # Запрещаем редактирование текстового поля
        self.text.configure(state='disabled')
