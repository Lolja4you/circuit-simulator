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


    # dup = [x for i, x in enumerate(parallel) if i != parallel.index(x)]
    # for i in dup:
#     #     components_dict[i]['parallel'] = True

# for i in components_dict:
#     print(components_dict[i])