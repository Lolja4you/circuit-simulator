from src.action_event import utils 

class Circuit:
    def __init__(self, ) -> None:
        self.name_circuit = 'test_1'
        self.components_matrix_incidence = {}
        
        """
                pk : objects 
            {
                1  : node object\n
                2  : resi object\n
                3  : capa object\n
                4  : node object\n
                5  : curr object\n
            }
        """
        self.components_matrix_adjacency = {}
        """
            {
                1   : [component]\n
                2   : [component]\n
                3   : [component]\n
                4   : [component]\n
                5   : [component]\n
            }
        
        """
        self.adjacency_dict = {}

        """
            node.pk : list[node.pk]
            {
                1   : [2, 3, 4]\n
                2   : [1, 3, 6]\n
                3   : [2, 1, 6]\n
                4   : [1, 2, 6]\n
                5   : [6, 7, 8]\n
                6   : [2, 3, 4, 5]\n
            }
        """
        self.current_contour = []

        self.resistance_dict = {}
        self.capacitor_dict = {}
        self.transistor_dict = {}
        self.key_dict = {}
        self.current_dict = {}
        self.current_voltage_dict = {}

        self.result: list

    def show_circuit(self) -> str:
        for key, items in self.components_matrix_incidence.items():
            print(f'{key} : {items}')

        for key, items in self.components_matrix_adjacency.items():
            print(f'{key} : {items}')

    def show_all_components(self) -> str:
        for key, items in self.components_matrix_incidence.items():
            print(f'{key} : {items}')

    def show_connection(self) -> str:
        for key, items in self.adjacency_dict.items():
            print(f'{key} : {items}')
    
    def is_closed(self) -> bool:
        """ recursive function """
        ...
    