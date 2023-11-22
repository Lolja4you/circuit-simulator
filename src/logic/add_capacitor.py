from src.core.components_api_2 import Capacitor
from src.action_event import utils


def input_capacitor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    capacitance = float(input('укажите ёмкость: '))
    angle = int(input('укажите угол наклона: '))
    if capacitance < 1e-3 or  capacitance > 0.005:
        return print(f'допустимый диапазон ёмкости. {capacitance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    add_capacitor(
        x, y, 
        capacitance,
        angle,
        circuit
    )

def add_capacitor(x, y, inductance, angle, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    capacitor = Capacitor(x, y, pk, inductance, angle=angle)
    
    circuit.components_matrix_incidence[capacitor.node_pk] = capacitor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

