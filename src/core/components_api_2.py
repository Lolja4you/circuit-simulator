class two_dimensions:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x} -- y: {self.y}'
        
class Node(two_dimensions):
    def __init__(self, x, y, node_pk: int) -> None:
        self.node_pk    = node_pk
        self.viewed     = False
        super().__init__(x, y)

    def change_viewed(self):
        self.viewed = True
    
    def __str__(self) -> str:
        return (
            f'{self.node_pk}\n{self.children}\n{self.parent}\n{self.viewed}'
        )

class Resistor(Node):
    def __init__(self, x, y, node_pk, resistance, pk) -> None:
        super().__init__(x, y, node_pk)
        self.name = f'R{pk}'
        self.resistance = resistance

    def __str__(self) -> str:
        return f'name: {self.name}\nx: {self.x} y: {self.y}\nresistance: {self.resistance}'
    
        
class Source(Node):
    def __init__(self, x, y, node_pk: int, amplitude, type_src: str, ac_dc = 'ac', frequency = 40) -> None:
        super().__init__(x, y, node_pk)
        self.node_pk = node_pk
        self.name = self.get_type(type_src)
        self.amplitude = amplitude
        self.ac, self.dc = ac_dc
        self.frequency = frequency

    def get_type(self, type_src):
        if type_src == 'voltage':
            return f'E{self.node_pk}'
        elif type_src == 'amper':
            return f'I{self.node_pk}'
        else:
            return self.get_type(type_src)


class Capacitor(Node):
    def __init__(self, x, y, node_pk: int, capacitance: float) -> None:
        super().__init__(x, y, node_pk)
        self.name = f'C{self.node_pk}'
        self.capacitance = capacitance


class Inductor(Node):
    def __init__(self, x, y, node_pk: int, inductance: float) -> None:
        super().__init__(x, y, node_pk)
        self.name = f'L{self.node_pk}'
        self.inductance = inductance