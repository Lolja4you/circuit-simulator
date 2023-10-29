components_dict ={
    1 : {'node_pk': 1, 
         'viewed': False, 
         'x': 10, 'y': 10, 
         'name': 'E1', 
         'amplitude': 10.0, 
         'ac': True, 
         'dc': False, 
         'parallel': False,
         'frequency': 60},
    2 : {'node_pk': 2, 'viewed': False, 'x': 10, 'y': 10, 'name': 'R2', 'parallel': False, 'resistance': 1000.0},
    3 : {'node_pk': 3, 'viewed': False, 'x': 10, 'y': 10, 'name': 'C3', 'parallel': False, 'capacitance': 0.001},
    4 : {'node_pk': 4, 'viewed': False, 'x': 10, 'y': 10, 'name': 'L4', 'parallel': False, 'inductance': 0.01},
}

connection_dict ={
    1 : [2],
    2 : [3],
    3 : [4],
    4 : [1],
}


conduction_matrix = []
current_matrix = []


parallel = []
voltage_matrix = []
def dfs(graph, start_node, visited, traversal, loops):
    visited[start_node] = True
    traversal.append(start_node)
    if len(connection_dict[start_node]) > 1:
        components_dict[start_node]['parallel'] = True
        for i in connection_dict[start_node]:
            parallel.append(i)
    else:
        for i in connection_dict[start_node]:
            parallel.append(i)
    
    dup = [x for i, x in enumerate(parallel) if i != parallel.index(x)]
    for i in dup:
        components_dict[i]['parallel'] = True

    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, traversal, loops)
        elif neighbor in traversal[:-1]:
            loop = traversal[traversal.index(neighbor):]
            loops.append(loop)
    
# Создаем граф в виде словаря смежности

# Инициализируем список посещенных вершин, список для сохранения обхода и список для сохранения контуров
visited = {node: False for node in connection_dict}
traversal = []
loops = []
branches = []
# Вызываем функцию обхода графа в глубину
dfs(connection_dict, 1, visited, traversal, loops)

# Выводим обход графа и контуры на экран
print("Обход графа:", traversal)
print("Контуры без учета источников напряжений:", loops)


####################
####################
####################

def created_branch(graph, start_node, branches, branch=[]):
    # traversal.append(start_node)
    if not components_dict[start_node]['parallel']:
        element = start_node
        branch.append(element)
    else:
        branch = [start_node]
        branches.append(branch)
    for neighbor in graph[start_node]:
        if not components_dict[neighbor]['viewed']:
            components_dict[neighbor]['viewed'] = True
            created_branch(graph, neighbor, branches, branch)
####################

branch = []
traversal = []
branches = []
created_branch(connection_dict, 1, branches)
print('br', branches)

####################
####################
####################

# Создаем массив точек для каждого контура
def create_voltage_matrix():
    for loop_points in loops:
        voltage = False
        for point in loop_points:
            if 'E' in components_dict[point]['name']:
                voltage_matrix.append(components_dict[point]['amplitude'])
                loop_points.remove(point)
                voltage = True
        if not voltage:
            point = 0
            voltage_matrix.append(point)
        else:... 
    print('матрица напряжений = матрице контуров: ', voltage_matrix, '=', loops)

create_voltage_matrix()


# Вычисляем общий ток для каждого контура
def calculated_resistant(
    common_resistance = 0,
    lol = []
):
    for loop_points in loops:
        for point in loop_points:
            if 'resistance' in components_dict[point]:
                resistance = components_dict[point]['resistance']
            elif 'capacitance' in components_dict[point]:
                resistance = -1 / (2 * 3.14159265359 * 60 * components_dict[point]['capacitance'])
            elif 'inductance' in components_dict[point]:
                resistance = (2 * 3.14159265359 * 60 * components_dict[point]['inductance'])
            common_resistance += resistance
            lol.append(point)
        
        loops[loops.index(loop_points)] = [common_resistance]
        common_resistance = 0
        # print(lol)
    # dup = [x for i, x in enumerate(lol) if i != lol.index(x)]
    # print(dup)
calculated_resistant()
print(loops, voltage_matrix) 



# for i in components_dict:
#     print(components_dict[i])



import numpy as np

A = np.array(loops)
b = np.array(voltage_matrix)

x = np.linalg.solve(A, b)

print(x)
voltage_list = []
for voltage in components_dict:
    name = components_dict[voltage]['name'] 
    if 'R' in name:
        volt = x[0] * components_dict[voltage]['resistance'] 
        power = x[0]**2 *  components_dict[voltage]['resistance']
    elif 'C' in name:
        volt = x[0] / (2 * 3.14159265359 * 60 *  components_dict[voltage]['capacitance'])
        power = x[0]**2 / ( 2 * 3.14159265359 * 60 * components_dict[voltage]['capacitance']) / 2
    elif 'L' in name:
        volt = x[0] * 2 * 3.14159265359 * 60 * components_dict[voltage]['inductance'] 
        power = x[0]**2 * 2 * 3.14159265359 * 60 * components_dict[voltage]['inductance'] /2 
    if "E" in name: voltage_list.append((name, components_dict[voltage]['amplitude'], x[0], components_dict[voltage]['amplitude']*x[0]))
    else: voltage_list.append((name, volt, x[0], power))

print('name   voltage(V) current(A)')
for el in voltage_list:
    print(voltage_list[voltage_list.index(el)])


import tkinter as tk
import math

def draw_resistor(x_1, y_1, x_2, y_2, angle):
    delta_y = y_1 - y_2
    if delta_y == 40:
        ...

    elif delta_y < 0:
        y_2 += 40 + delta_y

    else:
        y_2 += 40 + delta_y

    print(delta_y)

    delta_x = x_1 - x_2
    if delta_x == 100:
        ...

    elif delta_x < 0:
        x_2 += 100 + delta_x

    else:
        x_2 += 100 + delta_x
    print(delta_x)
    window = tk.Tk()
    window.title("Резистор")

    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack()

    # Поворачиваем координаты точек x_1, y_1, x_2, y_2
    angle_rad = math.radians(angle)
    x_1_rot = x_1 * math.sin(angle_rad) - y_1 * math.cos(angle_rad)
    y_1_rot = x_1 * math.cos(angle_rad) + y_1 * math.sin(angle_rad)
    x_2_rot = x_2 * math.sin(angle_rad) - y_2 * math.cos(angle_rad)
    y_2_rot = x_2 * math.cos(angle_rad) + y_2 * math.sin(angle_rad)

    # Поворачиваем координаты точек для ножек резистора
    y_start_rot = y_1_rot + abs(y_1_rot - y_2_rot) / 2


    # Рисуем повернутые линии вместо квадрата
    canvas.create_line(x_1_rot, y_1_rot, x_2_rot, y_1_rot)
    canvas.create_line(x_2_rot, y_1_rot, x_2_rot, y_2_rot)
    canvas.create_line(x_2_rot, y_2_rot, x_1_rot, y_2_rot)
    canvas.create_line(x_1_rot, y_2_rot, x_1_rot, y_1_rot)
    
    # Рисуем повернутые ножки резистора
    canvas.create_oval(x_1_rot - 48, y_start_rot - 2, x_1_rot - 52, y_start_rot + 2)
    canvas.create_oval(x_2_rot + 48, y_start_rot - 2, x_2_rot + 52, y_start_rot + 2)

    window.mainloop()


draw_resistor(100, 10, 10, -10, 0)

def draw_capacitor(x_1, y_1, x_2, y_2):
    # Создаем окно
    window = tk.Tk()
    window.title("Конденсатор")

    # Создаем Canvas для рисования
    canvas = tk.Canvas(window, width=200, height=100)
    canvas.pack()

    # Рисуем конденсатор
    canvas.create_line(40, 50, 60, 50) #правый лапка
    canvas.create_line(60, 10, 60, 90) #правая пластина
    canvas.create_line(75, 50, 95, 50) #правый лапка
    canvas.create_line(75, 10, 75, 90) #левая пластина

    # Запускаем главный цикл окна
    window.mainloop()


# draw_capacitor(10, 10, 10, 10)