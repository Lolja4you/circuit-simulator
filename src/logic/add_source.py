from src.core.components_api_2 import Source
from src.action_event import utils


def get_ac_dc(ac_dc = None):
    if ac_dc == 'ac':
        return True, False
    elif ac_dc == 'dc':
        return False, True
    else:
        return get_ac_dc(str(input('укажите ac/dc default="ac": ')))

def input_source_data(circuit):
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    get_type = str(input('укажите тип источника (voltage/amper): ')).lower()
    ac_dc = get_ac_dc()
    amplitude = float(input('укажите амплитутду: '))
    frequency = int(input('укажите частоту: '))
    add_source(
        x, y, 
        get_type,
        ac_dc,
        amplitude,
        frequency,
        circuit,
    )

def add_source(
        x, y, 
        get_type,
        ac_dc,
        amplitude,
        frequency,
        circuit
    ):
    pk = utils.get_last_pk(circuit.components_matrix_incidence) + 1
            
    source = Source(x, y, pk, amplitude, get_type, ac_dc, frequency)
    
    circuit.components_matrix_incidence[source.node_pk] = source.__dict__

    # connect.add_connection_manually(pk, node.add_node(x+30, y, circuit), circuit)
    # connect.add_connection_manually(pk, node.add_node(x-30, y, circuit), circuit)

