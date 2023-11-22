class two_dimensions:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x} -- y: {self.y}'
        
class Node(two_dimensions):
    def __init__(self, x, y, node_pk: int, angle = 0) -> None:
        self.node_pk    = node_pk
        self.viewed     = False
        super().__init__(x, y)
        self.length = 100 
        self.angle = angle
        self.color = "white"
        self.parallel = False 

    def change_viewed(self):
        self.viewed = True
    
    def __str__(self) -> str:
        return (
            f'{self.node_pk}\n{self.children}\n{self.parent}\n{self.viewed}'
        )

class Resistor(Node):
    def __init__(
        self, x, y, 
        node_pk, 
        resistance, 
        pk,
        angle,
    ) -> None:
        super().__init__(x, y, node_pk, angle)
        self.type = 'resistor'

        self.name = f'R{pk}'
        self.resistance = resistance
        self.length = 100
        self.color = "white"
        self.parallel = False 

    def __str__(self) -> str:
        return f'name: {self.name}\nx: {self.x} y: {self.y}\nresistance: {self.resistance}'
    
        
class Source(Node):
    def __init__(self, x, y, node_pk: int, amplitude, type_src: str,        
        angle = 0,
        ac_dc = 'ac', frequency = 40,
    ) -> None:
        
        super().__init__(x, y, node_pk, angle)
        self.node_pk = node_pk
        self.name = self.get_type(type_src)
        self.amplitude = amplitude
        self.ac, self.dc = ac_dc
        self.frequency = frequency
        self.length = 100
        self.color = "white"
        self.parallel = False
        self.type = 'source' 


    def get_type(self, type_src):
        if type_src == 'voltage':
            return f'E{self.node_pk}'
        elif type_src == 'amper':
            return f'I{self.node_pk}'
        else:
            return self.get_type(type_src)


class Capacitor(Node):
    def __init__(self, x, y, node_pk: int, capacitance, angle=0) -> None:
        super().__init__(x, y, node_pk, angle)
        self.name = f'C{self.node_pk}'
        self.capacitance = capacitance
        self.length = 100
        self.color = "white"
        self.parallel = False 
        self.type = 'capacitor'



class Inductor(Node):
    def __init__(self, x, y, node_pk: int, inductance, angle=0) -> None:
        super().__init__(x, y, node_pk, angle)
        
        super().__init__(x, y, node_pk, angle)
        self.name = f'L{self.node_pk}'
        self.inductance = inductance
        self.length = 100
        self.color = "white"
        self.parallel = False 
        self.type = 'inductor'
