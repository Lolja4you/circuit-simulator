import tkinter as tk
from tkinter import messagebox

from src.core.components_api_2 import Capacitor
from src.action_event import utils


def input_capacitor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    capacitance = float(input('укажите ёмкость: '))
    angle = int(input('укажите угол наклона: '))
    if capacitance < 1e-3 or  capacitance > 0.005:
        return print(f'допустимый диапазон ёмкости. {capacitance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    add_capacitor(
        x, y, 
        capacitance,
        angle,
        circuit
    )

def UI_input_capacitor_data(circuit, parent):
    def check_add_capacitance():
        x = int(x_entry.get())
        y = int(y_entry.get())
        capacitance = float(inductance_entry.get())
        angle = int(angle_entry.get())

        if capacitance < 1e-3 or  capacitance > 0.005:
            messagebox.showerror("Ошибка", "Допустимый диапазон ёмкости: (1e-3)-0.005 (Ф).")
            return

        if abs(x) > 2000 or abs(y) > 2000:
            messagebox.showerror("Ошибка", "Допустимый диапазон координат X и Y: -2000 до 2000.")
            return

        if abs(angle) > 360:
            messagebox.showerror("Ошибка", "Допустимый диапазон угла наклона: -360 до 360.")
            return

        add_capacitor(x, y, capacitance, angle, circuit)
        messagebox.showinfo("Успех", "Конденсатор успешно добавлен.")
        parent.re_draw()
        root.destroy()


    root = tk.Tk()
    root.title("Ввод данных конденсатора")

    x_label = tk.Label(root, text="Укажите точку X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()

    y_label = tk.Label(root, text="Укажите точку Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    inductance_label = tk.Label(root, text="Укажите ёмкость:")
    inductance_label.pack()
    inductance_entry = tk.Entry(root)
    inductance_entry.pack()

    angle_label = tk.Label(root, text="Укажите угол наклона:")
    angle_label.pack()
    angle_entry = tk.Entry(root)
    angle_entry.pack()

    add_button = tk.Button(root, text="Добавить конденсатор", command=check_add_capacitance)
    add_button.pack()

    root.mainloop()

def add_capacitor(x, y, capacitance, angle, circuit):
    node_pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    res_pk = utils.get_last_pk(circuit.capacitor_count) + 1
    
    capacitor = Capacitor(
                x, y, 
                node_pk=node_pk, 
                type_pk=res_pk, 
                angle=angle,
                capacitance=capacitance, 
    )
    
    circuit.components_matrix_incidence[capacitor.node_pk] = capacitor.__dict__
    circuit.capacitor_count[capacitor.node_pk] = capacitor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

