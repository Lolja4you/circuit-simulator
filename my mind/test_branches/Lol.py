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
    5 : {'node_pk': 5, 'viewed': False, 'x': 10, 'y': 10, 'name': 'R5', 'parallel': False, 'resistance': 1000.0},
}


connection_dict ={
    1 : [2, 5],
    2 : [3],
    3 : [4],
    4 : [1],
    5 : [4],
}


conduction_matrix = []
current_matrix = []


def dfs(graph, start_node, visited, traversal, loops):
    visited[start_node] = True
    traversal.append(start_node)
    parallel = [] # Define the 'parallel' list here
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

visited = {node: False for node in connection_dict}
traversal = []
loops = []
branches = []
dfs(connection_dict, 1, visited, traversal, loops)

print("Обход графа:", traversal)
print("Контуры без учета источников напряжений:", loops)


def created_branch(graph, start_node, branches, branch=[]):
    if not components_dict[start_node]['parallel']:
        element = start_node
        branch.append(element)
    else:
        if len(connection_dict[start_node]) == 1:
            element = start_node
            branch.append(element)
        else:
            branch = [start_node]
            branches.append(branch)
    for neighbor in graph[start_node]:
        if not components_dict[neighbor]['viewed']:
            components_dict[neighbor]['viewed'] = True
            created_branch(graph, neighbor, branches, branch)


branch = []
traversal = []
branches = []
created_branch(connection_dict, 1, branches)
print('br', branches)


def create_voltage_matrix():
    for loop_points in branches:
        voltage = False
        for point in loop_points:
            if 'E' in components_dict[point]['name']:
                voltage_matrix.append(components_dict[point]['amplitude'])
                loop_points.remove(point)
                voltage = True
        if not voltage:
            voltage_matrix.append(0)

def remove_from_loops():
    for loop_points in loops:
        for point in loop_points:
            if 'E' in components_dict[point]['name']:
                loop_points.remove(point)
remove_from_loops()

voltage_matrix = []
create_voltage_matrix()
print('матрица напряжений = матрице контуров: ', voltage_matrix, '=', loops)


def mem(kek=[], common_resistance = 0):
    common_values = set(kek[0])
    for points in kek[1:]:
        common_values &= set(points)

    kek = list(common_values)
    for point in kek:
        if 'resistance' in components_dict[point]:
            resistance = components_dict[point]['resistance']
        elif 'capacitance' in components_dict[point]:
            resistance = -1 / (2 * 3.14159265359 * 60 * components_dict[point]['capacitance'])
        elif 'inductance' in components_dict[point]:
            resistance = (2 * 3.14159265359 * 60 * components_dict[point]['inductance'])
        common_resistance += resistance
    return -common_resistance
        

def calculated_resistant():
    result = mem(loops)
    for loop_points in loops:
        common_resistance = 0
        for point in loop_points:
            if 'resistance' in components_dict[point]:
                resistance = components_dict[point]['resistance']
            elif 'capacitance' in components_dict[point]:
                resistance = -1 / (2 * 3.14159265359 * 60 * components_dict[point]['capacitance'])
            elif 'inductance' in components_dict[point]:
                resistance = (2 * 3.14159265359 * 60 * components_dict[point]['inductance'])
            print(components_dict[point]['name'], resistance)
            common_resistance += resistance
        loop_points.clear()
        loop_points.append(common_resistance)
        print(result)
        loop_points.append(result)


calculated_resistant()
print(loops, voltage_matrix)

import numpy as np


A = np.array([[1001.1173287994432, -3.769911184308], [3.76991118430, 1003.769911184308]])
B = np.array(voltage_matrix)
X = np.linalg.solve(A, B)
print('es ', X)