import tkinter as tk
from tkinter import ttk

from src.utils import check_result


class Table(tk.Tk):
    def __init__(self, circuit_init):
        super().__init__()
        
        self.circuit_init = circuit_init
        self.is_init = check_result.is_result(circuit_init)

        self.x = self.winfo_screenwidth()
        self.y = self.winfo_screenheight()
        self.title("test_1 - table") 
        self.configure(bg='#030B15')

        width = int(round(self.x/1.5, 0))
        height = int(round(self.y/1.1, 0))

        x_position = -10
        y_position = 0
        self.geometry(f"{width}x{height}+{x_position}+{y_position}")
        
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Name", "Voltage(V)", 'voltagedrop(V)', "Current(A)", "power(W)")
        
        # Устанавливаем заголовки столбцов
        self.tree.heading("#0", text="Index")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Voltage(V)", text="Voltage(V)")
        self.tree.heading('voltagedrop(V)', text='voltagedrop(V)')
        self.tree.heading("Current(A)", text="Current(A)")
        self.tree.heading("power(W)", text="Power(W)")
        
        # Добавляем кортежи в таблицу
        tuples = self.circuit_init.result
        
        for i, row in enumerate(tuples):
            self.tree.insert("", i, text=f"{i+1}", values=row)
        
        # Размещаем Treeview на форме
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        # Изменяем цвет таблицы и шрифта, а также ширину колонок и цвет разделителей
        style = ttk.Style()
        style.configure("Treeview", background="#2B2B2B", foreground="white", fieldbackground="#2B2B2B")        
        style.configure("Treeview.Heading", background="#030B15", foreground="white", font=("Arial", 10, "bold"))
        style.configure("Treeview.Separator", background="white")
        self.tree.configure(style="Treeview")