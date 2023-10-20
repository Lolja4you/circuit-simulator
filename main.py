from src.logic import add_nodes as node
from src.logic import add_resistors as resistor
from src.logic import add_connection as connetcion
from src.logic import add_source as source
from src.logic import add_capacitor as capacitor
from src.logic import add_inductor as inductor

from src.core import find_counters as contour

from src.action_event.action_files import save_circuit as save

from src.UI import start_UI  as UI


from src.core import circuit_api_2
circuit_init = circuit_api_2.Circuit()

def show_menu():
    menu =  """
        0) add Branch
        1) add Current source
        2) add Resistor
        3) add Capacitor
        4) add Inductor
        
        *) show circuit

        +) add connection(auto) 
        ++) add connection manually

        -) undo last action
        --) clear all

        'start' for start UI

        'save' for save circuit

        'exit' for exit
        
        input 1-5 or exit/start
        """
    print(menu)

def user_choose():


    choose = input("--> ")
    
    match choose:
        # case "0": input_branch()
        case "0": node.input_node(circuit_init)
        case "1": source.input_source_data(circuit_init)
        case "2": resistor.input_resistor_data(circuit_init)
        case "3": capacitor.input_capacitor_data(circuit_init)
        case "4": inductor.input_inductor_data(circuit_init)

        case "*": circuit_init.show_circuit()
        case "**": circuit_init.show_all_components()
        case "***": circuit_init.show_connection()

        # case "+": connetcion.add_connetction(circuit_init)
        case "++": connetcion.input_connection_manually(circuit_init)
        
        case "-": undo_last_action()
        case "--": clear_all()

        case "start": UI.init_UI()
        case "save" : save.save_circuit(circuit_init)
        case "open" : save.open_circuit(str(input("имя файла: ")), circuit_init)
        case "exit" : return quit()

        case "xxx"  :  contour.node_method_potential(circuit_init)


while True:
    show_menu()
    user_choose()