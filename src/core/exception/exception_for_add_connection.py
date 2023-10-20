def is_exist(node, circuit):
    try:
        circuit.components_matrix_incidence[node]
    except KeyError:
        raise(f'error: not exist node.\nnode: {node}')
    

def is_equal(node_first, node_second, circuit):
    if node_first != node_second:
        pass
        ...
    else:
        raise(f"error: You can't connected equal node\nnode first: {node_first} -> node second: {node_second}")
    
    try:                                                                                                        ### check with error
        circuit.adjacency_dict[node_first].index(node_second)                                                   ###
        raise(f'error: these nodes are already connected\nnode first: {node_first} node second: {node_second}') ###                              
    except ValueError: ...                                                                                      ### check accept
        

def is_lol(circuit):
    ...