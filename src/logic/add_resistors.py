from src.core.components_api_2 import Resistor
from src.logic import add_nodes as node
from src.logic import add_connection as connect

from src.action_event import utils


def input_resistor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    resistance = float(input('укажите сопротивление: '))
    add_resistor(
        x, y, 
        resistance,
        circuit
    )

def add_resistor(x, y, resistance, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    resistor = Resistor(x, y, pk, resistance, pk)
    
    circuit.components_matrix_incidence[resistor.node_pk] = resistor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

