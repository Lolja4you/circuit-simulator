def is_valid_connection(ciruit:object, first_node:int, last_node:int):
    """
    ciruit:object, 
    first_node:int, last_node:int must be pk value from circuit.components_matrix_incidence
    """
    connection = ciruit.adjacency_dict
    for i in connection:
        id_list = [i]
        for el in connection[i]:
            id_list.append(el)
        try:
            id_list.index(first_node)
            id_list.index(last_node)
            return False
        
        except ValueError:...

    return True

def check_node_in_adjacency_dict(circuit, node):
    try:
        circuit[node]
    except KeyError:
        circuit[node] = []