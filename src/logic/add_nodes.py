from src.core.components_api_2 import Node
from src.action_event import utils

def input_node(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    add_node(x, y, circuit)
    
def add_node(x, y, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    node = Node(x,y, pk)
    circuit.components_matrix_incidence[node.node_pk] = node.__dict__
    #circuit.adjacency_dict[node.node_pk] = 
    #record_last_action
    return pk
