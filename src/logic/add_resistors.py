from src.core.components_api_2 import Resistor
from src.logic import add_nodes as node
from src.logic import add_connection as connect

from src.action_event import utils


def input_resistor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    resistance = float(input('укажите сопротивление: '))
    angle = int(input('укажите угол наклона: '))
    if resistance < 1 or resistance > 1000:
        return print(f'допустимый диапазон 1-1000(ОМ). {resistance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    add_resistor(
        x, y, 
        resistance,
        angle,
        circuit,
    )

def add_resistor(x, y, resistance, angle, circuit):
    print(angle)
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    resistor = Resistor(x, y, pk, resistance, pk, angle=angle)
    print(resistor.__dict__)
    circuit.components_matrix_incidence[resistor.node_pk] = resistor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

