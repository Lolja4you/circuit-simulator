from src.action_event import utils
import numpy as np

def node_method_potential_0_0(circuit):
    matrix_size = utils.get_last_pk(circuit.components_matrix_incidence) - 1
    num_edges = utils.get_last_pk(circuit.components_matrix_adjacency, ) - 1
    A = [[0] * (matrix_size) for _ in range(matrix_size)]
    b = [0] * (matrix_size)
    print(A, b)
    # Заполнение матрицы A и вектора b
    for i in range(matrix_size):
        print(i)
        for j in range(matrix_size):
            print(j)
            if i == j:...
                # A[i][j] = sum(circuit.components_matrix_incidence[k][i] for k in range(num_edges))
            else:
                print(A[i][j], circuit.components_matrix_incidence[f'{i}'])
                

        # b[i] = sum(circuit.incidence_matrix[k][i] * circuit.components_matrix_incidence[k+1][i+1]['value']
        #         for k in range(num_edges) if isinstance(circuit.components_matrix_incidence[k+1][i+1], VoltageSource))
        

def node_method_potential(circuit):
    matrix_size = utils.get_last_pk(circuit.components_matrix_adjacency) - 1
    true_matrix_size = 0
    branch_matrix = {}
    n = 0
    for branch in circuit.components_matrix_adjacency:
        if len(circuit.components_matrix_adjacency[branch]) > 1:
            branch_matrix[f'{n+1}'] = [circuit.components_matrix_incidence[branch]]
        else:
            try:
                branch_matrix[f'{n+1}'].append(circuit.components_matrix_incidence[branch])
            except KeyError:
                branch_matrix[f'{n+1}'] = [circuit.components_matrix_incidence[branch]]

    print(f'matrix size: {matrix_size}\ntrue matrix size: {len(branch_matrix.keys())}\nbranch: {branch_matrix}')