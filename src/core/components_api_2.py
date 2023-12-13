class two_dimensions:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x} -- y: {self.y}'
        
class Node(two_dimensions):
    def __init__(self, x, y, node_pk: int, angle: int = 0, type_pk: int = None) -> None:
        self.node_pk    = node_pk
        self.type_pk    = type_pk
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
        self, *args,
        resistance, 
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.type = 'resistor'

        self.name = f'R{self.type_pk}'
        self.resistance = resistance
        self.length = 100
        self.color = "white"
        self.parallel = False 

    def __str__(self) -> str:
        return f'name: {self.name}\nx: {self.x} y: {self.y}\nresistance: {self.resistance}'
    
        
class Source(Node):
    def __init__(
        self, *args, 
        amplitude, 
        type_src: str,        
        ac_dc = 'ac', 
        frequency = 40,
        **kwargs,
    ) -> None:
        
        super().__init__(*args, **kwargs)
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
            return f'E{self.type_pk}'
        elif type_src == 'amper':
            return f'I{self.type_pk}'
        else:
            return self.get_type(type_src)


class Capacitor(Node):
    def __init__(
        self, *args,
        capacitance, 
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.name = f'C{self.type_pk}'
        self.capacitance = capacitance
        self.length = 100
        self.color = "white"
        self.parallel = False 
        self.type = 'capacitor'



class Inductor(Node):
    def __init__(
        self, *args,
        inductance, 
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.name = f'L{self.type_pk}'
        self.inductance = inductance
        self.length = 100
        self.color = "white"
        self.parallel = False 
        self.type = 'inductor'
