from src.core.components_api_2 import Inductor
from src.action_event import utils


def input_inductor_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    inductance = float(input('укажите индуктивность: '))
    angle = int(input('укажите угол наклона: '))
    if inductance < 0.05 or  inductance > 0.1:
        return print(f'допустимый диапазон индуктивности. {inductance}')
    if (x or y) > 2000 or (x or y) < -2000:
        return print(f'допустимый диапазон x, y. {x, y}')
    if abs(angle) > 360:
        return print(f'допустимый диапазон angle. {angle}')
    add_inductor(
        x, y, 
        inductance,
        angle,
        circuit
    )

def add_inductor(x, y, inductance, angle, circuit):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
    
    inductor = Inductor(x, y, pk, inductance, angle=angle)
    
    circuit.components_matrix_incidence[inductor.node_pk] = inductor.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

