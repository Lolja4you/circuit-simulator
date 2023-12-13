import tkinter as tk
from tkinter import messagebox

from src.core.components_api_2 import Inductor
from src.action_event import utils


def input_inductor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    inductance = float(input('укажите индуктивность: '))
    angle = int(input('укажите угол наклона: '))
    if inductance < 0.05 or  inductance > 0.1:
        return print(f'не допустимый диапазон индуктивности. {inductance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'не допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'не допустимый диапазон angle. {angle}')
    add_inductor(
        x, y, 
        inductance,
        angle,
        circuit
    )

def UI_input_inductor_data(circuit, parent):
    def check_add_inductor():
        x = int(x_entry.get())
        y = int(y_entry.get())
        inductance = float(inductance_entry.get())
        angle = int(angle_entry.get())

        if inductance < 0.05 or inductance > 0.1:
            messagebox.showerror("Ошибка", "Допустимый диапазон индуктивности: 0.05-0.1 (Гн).")
            return

        if abs(x) > 2000 or abs(y) > 2000:
            messagebox.showerror("Ошибка", "Допустимый диапазон координат X и Y: -2000 до 2000.")
            return

        if abs(angle) > 360:
            messagebox.showerror("Ошибка", "Допустимый диапазон угла наклона: -360 до 360.")
            return

        add_inductor(x, y, inductance, angle, circuit)
        messagebox.showinfo("Успех", "Индуктивность успешно добавлена.")
        parent.re_draw()
        root.destroy()


    root = tk.Tk()
    root.title("Ввод данных индуктивности")

    x_label = tk.Label(root, text="Укажите точку X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()

    y_label = tk.Label(root, text="Укажите точку Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    inductance_label = tk.Label(root, text="Укажите индуктивность:")
    inductance_label.pack()
    inductance_entry = tk.Entry(root)
    inductance_entry.pack()

    angle_label = tk.Label(root, text="Укажите угол наклона:")
    angle_label.pack()
    angle_entry = tk.Entry(root)
    angle_entry.pack()

    add_button = tk.Button(root, text="Добавить индуктивность", command=check_add_inductor)
    add_button.pack()

    root.mainloop()

def add_inductor(x, y, inductance, angle, circuit):
    node_pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    ind_pk = utils.get_last_pk(circuit.inductor_count) + 1

    inductor = Inductor(
                x, y, 
                node_pk=node_pk, 
                type_pk=ind_pk, 
                angle=angle,
                inductance=inductance, 
    )
    
    circuit.components_matrix_incidence[inductor.node_pk] = inductor.__dict__
    circuit.inductor_count[inductor.node_pk] = inductor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

