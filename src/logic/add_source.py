from src.core.components_api_2 import Source
from src.action_event import utils


def get_ac_dc(ac_dc = None):
    if ac_dc == 'ac':
        return True, False
    elif ac_dc == 'dc':
        return False, True
    else:
        return get_ac_dc(str(input('укажите ac/dc default="ac": ')))

def input_source_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    get_type = str(input('укажите тип источника (voltage/amper): ')).lower()
    ac_dc = get_ac_dc()
    amplitude = float(input('укажите амплитутду: '))
    frequency = int(input('укажите частоту: '))
    angle = int(input('укажите угол наклона: '))
    
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    if abs(amplitude) > 12:
        return print(f'допустимый диапазон амплитуды. {amplitude}')
    if frequency < 40 or frequency > 70:
        return print(f'допустимый диапазон частоты. {frequency}')
    if get_type == "amper":
        return print(f'в данный момент данная функция не достпуна. {get_type}')
    if ac_dc == "ac":
        return print(f'в данный момент данная функция не достпуна. {ac_dc}')
    
    add_source(
        x, y, 
        get_type,
        ac_dc,
        amplitude,
        frequency,
        angle,
        circuit,
    )
import tkinter as tk
from tkinter import messagebox

def UI_input_source_data(circuit, parent):
    def check_add_source():
        x = int(x_entry.get())
        y = int(y_entry.get())
        get_type = type_entry.get().lower()
        ac_dc = get_ac_dc(ac_dc_entry.get())
        amplitude = float(amplitude_entry.get())
        frequency = int(frequency_entry.get())
        angle = int(angle_entry.get())

        if (x or y) > 2000 or (x or y) < -2000:
            messagebox.showerror("Ошибка", "Допустимый диапазон x, y: -2000 до 2000.")
            return

        if abs(angle) > 360:
            messagebox.showerror("Ошибка", "Допустимый диапазон angle: -360 до 360.")
            return

        if abs(amplitude) > 12:
            messagebox.showerror("Ошибка", "Допустимый диапазон амплитуды: -12 до 12.")
            return

        if frequency < 40 or frequency > 70:
            messagebox.showerror("Ошибка", "Допустимый диапазон частоты: 40 до 70.")
            return

        if get_type == "amper":
            messagebox.showerror("Ошибка", "В данный момент данная функция не доступна.")
            return

        if ac_dc == (True, False):
            messagebox.showerror("Ошибка", "В данный момент данная функция не доступна.")
            return

        add_source(x, y, get_type, ac_dc, amplitude, frequency, angle, circuit)
        messagebox.showinfo("Успех", "Источник успешно добавлен.")
        parent.re_draw()
        root.destroy()

    root = tk.Tk()
    root.title("Ввод данных источника")

    x_label = tk.Label(root, text="Укажите точку X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()

    y_label = tk.Label(root, text="Укажите точку Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    type_label = tk.Label(root, text="Укажите тип источника (voltage/amper):")
    type_label.pack()
    type_entry = tk.Entry(root)
    type_entry.pack()

    ac_dc_label = tk.Label(root, text="Укажите тип тока (ac/dc):")
    ac_dc_label.pack()
    ac_dc_entry = tk.Entry(root)
    ac_dc_entry.pack()

    amplitude_label = tk.Label(root, text="Укажите амплитуду:")
    amplitude_label.pack()
    amplitude_entry = tk.Entry(root)
    amplitude_entry.pack()

    frequency_label = tk.Label(root, text="Укажите частоту:")
    frequency_label.pack()
    frequency_entry = tk.Entry(root)
    frequency_entry.pack()

    angle_label = tk.Label(root, text="Укажите угол наклона:")
    angle_label.pack()
    angle_entry = tk.Entry(root)
    angle_entry.pack()

    add_button = tk.Button(root, text="Добавить источник", command=check_add_source)
    add_button.pack()

    root.mainloop()

def add_source(
        x, y, 
        get_type,
        ac_dc,
        amplitude,
        frequency,
        angle,
        circuit,
    ):
    node_pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    source_pk = utils.get_last_pk(circuit.source_count) + 1
    
    source = Source(
            x, y, 
            node_pk=node_pk, 
            type_pk=source_pk, 
            angle=angle,
            amplitude=amplitude, 
            frequency=frequency,
            ac_dc=ac_dc,
            type_src=get_type,
    )
    
    circuit.components_matrix_incidence[source.node_pk] = source.__dict__
    circuit.source_count[source.node_pk] = source.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

