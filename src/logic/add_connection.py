from src.core.exception import exception_for_add_connection as exceptions


def add_connetction(circuit):
    for key, items in circuit.components_matrix_incidence.items():
        x_item_first = items['x']
        y_item_first = items['y']
        pk = key
        circuit.adjacency_dict[pk] = []
        for key, items in circuit.components_matrix_incidence.items():
            if key != pk:
                x_item_second = items['x']
                y_item_second = items['y']
                if x_item_first == x_item_second and y_item_first == y_item_second:
                    circuit.adjacency_dict[pk].append(key)

def input_connection_manually(circuit):
    circuit.show_circuit()
    node_first  = int(input('укажите первый узел: '))
    node_second = int(input('укажите второй узел: '))

    ### check exception
    # exceptions.is_exist(node_first, circuit)
    # exceptions.is_exists(node_second, circuit)
    # exceptions.is_equal(node_first, node_second, circuit)

    ### add conection
    add_connection_manually(node_first, node_second, circuit)

def add_connection_manually(node_first, node_second, circuit):
    check_node_in_adjacency_dict(node_first, circuit)
    check_node_in_adjacency_dict(node_second, circuit)

    circuit.components_matrix_adjacency[f'{node_first}'].append(node_second)
    # circuit.components_matrix_adjacency[f'{node_second}'].append(node_first)

def check_node_in_adjacency_dict(node, circuit):
    try:
        circuit.components_matrix_adjacency[f'{node}']
    except KeyError:
        circuit.components_matrix_adjacency[f'{node}'] = []
    