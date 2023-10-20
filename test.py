components_dict ={
    1 : {'node_pk': 1, 
         'viewed': False, 
         'x': 10, 'y': 10, 
         'name': 'E1', 
         'amplitude': 10.0, 
         'ac': True, 
         'dc': False, 
         'frequency': 60},
    2 : {'node_pk': 2, 'viewed': False, 'x': 10, 'y': 10, 'name': 'R2', 'resistance': 10.0},
    3 : {'node_pk': 3, 'viewed': False, 'x': 10, 'y': 10, 'name': 'C3', 'capacitance': 0.001},
    4 : {'node_pk': 4, 'viewed': False, 'x': 10, 'y': 10, 'name': 'L4', 'inductance': 0.01},
    5 : {'node_pk': 5, 'viewed': False, 'x': 10, 'y': 10, 'name': 'C5', 'capacitance': 0.001},
    6 : {'node_pk': 6, 
         'viewed': False, 
         'x': 10, 'y': 10, 
         'name': 'E2', 
         'amplitude': 5.0, 
         'ac': True, 
         'dc': False, 
         'frequency': 60},
}
connection_dict ={
    1 : [2, 5],
    2 : [3],
    3 : [4],
    4 : [1],
    5 : [4],
    # 6 : [4],    
}

conduction_matrix = []
current_matrix = []

# [2, 3, 4]
# [10.0, 0.0002653927813163482, 3768.0]  =  [10.0]
# 0.0026469029374089643

voltage_matrix = []
def dfs(graph, start_node, visited, traversal, loops):
    visited[start_node] = True
    traversal.append(start_node)

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

# Вызываем функцию обхода графа в глубину
dfs(connection_dict, 1, visited, traversal, loops)

# Выводим обход графа и контуры на экран
print("Обход графа:", traversal)
print("Контуры без учета источников напряжений:", loops)

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

# Создаем словарь для хранения общих токов
current_dict = {}

# Вычисляем общий ток для каждого контура
for loop_points in loops:
    total_conductance = 0
    for point in loop_points:
        if point != 1 and point != 4:  # Исключаем узлы 1 и 4
            if 'resistance' in components_dict[point]:
                conductance = 1 / components_dict[point]['resistance']
            elif 'capacitance' in components_dict[point]:
                conductance = 1 / (2 * 3.14 * 60 * components_dict[point]['capacitance'])
            elif 'inductance' in components_dict[point]:
                conductance = 1 / (2 * 3.14 * 60 * components_dict[point]['inductance'])
            total_conductance += conductance
    current_dict[tuple(loop_points)] = voltage_matrix[loops.index(loop_points)] * total_conductance

# Выводим общие токи на экран
for loop_points, current in current_dict.items():
    print(f"Узлы {loop_points} имеют общий ток {current}")
