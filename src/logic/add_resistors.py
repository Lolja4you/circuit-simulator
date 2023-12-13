import tkinter as tk
from tkinter import messagebox

from src.core.components_api_2 import Resistor
from src.logic import add_nodes as node
from src.logic import add_connection as connect

from src.action_event import utils


def input_resistor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    resistance = float(input('укажите сопротивление: '))
    angle = int(input('укажите угол наклона: '))
    if resistance < 1 or resistance > 1000:
        return print(f'допустимый диапазон 1-1000(ОМ). {resistance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    add_resistor(
        x, y, 
        resistance,
        angle,
        circuit,
    )

def UI_input_resistor_data(circuit, parent):
    def check_add_resistor():
        x = int(x_entry.get())
        y = int(y_entry.get())
        resistance = float(resistance_entry.get())
        angle = int(angle_entry.get())

        if resistance < 1 or resistance > 1000:
            messagebox.showerror("Ошибка", "Допустимый диапазон сопротивления 1-1000 (Ом).")
            return

        if abs(x) > 2000 or abs(y) > 2000:
            messagebox.showerror("Ошибка", "Допустимый диапазон координат X и Y: -2000 до 2000.")
            return

        # if abs(angle) == (90 or 0):
        #     messagebox.showerror("Ошибка", "Допустимый диапазон угла наклона: -360 до 360.")
        #     return

        add_resistor(x, y, resistance, angle, circuit)
        messagebox.showinfo("Успех", "Резистор успешно добавлен.")
        parent.re_draw()
        root.destroy()


    root = tk.Tk()
    root.title("Ввод данных резистора")

    x_label = tk.Label(root, text="Укажите точку X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()

    y_label = tk.Label(root, text="Укажите точку Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    resistance_label = tk.Label(root, text="Укажите сопротивление:")
    resistance_label.pack()
    resistance_entry = tk.Entry(root)
    resistance_entry.pack()

    angle_label = tk.Label(root, text="Укажите угол наклона:")
    angle_label.pack()
    angle_entry = tk.Entry(root)
    angle_entry.pack()

    add_button = tk.Button(root, text="Добавить резистор", command=check_add_resistor)
    add_button.pack()

    root.mainloop()


def add_resistor(x, y, resistance, angle, circuit):
    node_pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    res_pk = utils.get_last_pk(circuit.resistor_count) + 1
    resistor = Resistor(
                round(x/25)*25, round(y/25)*25, 
                node_pk=node_pk, 
                type_pk=res_pk, 
                angle=angle,
                resistance=resistance, 
    )

    circuit.components_matrix_incidence[resistor.node_pk] = resistor.__dict__
    circuit.resistor_count[resistor.node_pk] = resistor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

