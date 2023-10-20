from src.core.components_api_2 import Capacitor
from src.action_event import utils


def input_capacitor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    capacitance = float(input('укажите ёмкость: '))
    add_capacitor(
        x, y, 
        capacitance,
        circuit
    )

def add_capacitor(x, y, inductance, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    capacitor = Capacitor(x, y, pk, inductance)
    
    circuit.components_matrix_incidence[capacitor.node_pk] = capacitor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

