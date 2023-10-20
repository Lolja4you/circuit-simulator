from src.core.components_api_2 import Inductor
from src.action_event import utils


def input_inductor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    inductance = float(input('укажите индуктивность: '))
    add_inductor(
        x, y, 
        inductance,
        circuit
    )

def add_inductor(x, y, inductance, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    inductor = Inductor(x, y, pk, inductance)
    
    circuit.components_matrix_incidence[inductor.node_pk] = inductor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

