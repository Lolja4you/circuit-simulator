class Point:
    def __init__(self, pk) -> None:
        self.pk = pk

    def __str__(self) -> str:
        return f"Point: {self.pk}"
    
class MainEntryPoint:
    def __init__(self, input_point, output_point):
        self.input_point = input_point
        self.output_point = output_point
    
    def __str__(self) -> str:
        return f"entry_1: {self.input_point}\nentry_2: {self.output_point}"
    
class Node:
    def __init__(self, pk) -> None:
        self.pk = pk

    def __str__(self) -> str:
        return f"Node: {self.pk}"

class Branch:
    # СУТЬ В ТОМ ЧТО pk_point --- ЭТО NODE-Ы ОДИН И ДВА, ДАЛЬШЕ МЫ БУДЕМ ЧЕКАТЬ ЗАМКНУТА ЛИ ЦЕПЬ. 
    def __init__(self, pk_point: tuple, list_components = []) -> None:
        self.entry = pk_point
        self.list_components = list_components
    
    def add_components(self, component: dict):
        self.list_components.append(component)
    
    def __str__(self) -> str:
        print(self.entry, self.list_components)

    def branch_serializer(self) -> dict:
        """возвращает словарь вида:
          data ={
                    "entry": (1, 2)(Это узлы Node),
                    "components": [
                        Resistor: {
                            "name": "Resistor 1",\n
                            "short_name": "R1",\n
                            "entry": (1,2)(Это точки входа MainEntryPoint),\n
                            "resistance": 20,
                        },
                        Capacitor: {...},\n
                        AC_Source: {...},    
                    ] 
                }
        """
        branch_data = {
            "entry_node": self.entry,
            "components": self.list_components
        }
        return branch_data

class Resistor(MainEntryPoint):
    def __init__(self, input_point, output_point, resistance, pk) -> None:
        super().__init__(input_point, output_point)
        self.name = f"Resistor:{pk}"
        self.short_name = f"R{pk}"
        self.resistance = resistance
        self.entry = (input_point, output_point)
        
    def resistor_serializer(self):
        return {
            "name" : self.name,
            "short_name": self.short_name,
            "entry_point": self.entry,
            "resistance": self.resistance,
        }
    
    def __str__(self) -> str:
        return super().__str__(), f"\nresistance: {self.resistance}"

class Capacitor(MainEntryPoint):
    def __init__(self, input_point, output_point, capacity, pk: int) -> dict:
        super().__init__(input_point, output_point)
        self.name = f"Capacitor_pk:{pk}"
        self.short_name = f"C{pk}"
        self.capacity = capacity
        self.entry = (input_point, output_point)

        return {
            "name" : self.name,
            "short_name": self.short_name,
            "entry_point": self.entry,
            "capacity": self.capacity,
        }
        
    def __str__(self) -> str:
        return super().__str__(), f"\ncapacity: {self.capacity}"

class Inductor:
    ...

class SourceCurrent(MainEntryPoint):
    def __init__(
                self, input_point, output_point,
                voltage=None, current=None,
                internal_resistance=0,):
        super().__init__(input_point, output_point)

        self.voltage = voltage
        self.current = current
        self.internal_resistance = internal_resistance
        self.entry = (input_point, output_point)
        self.type = None

    def type_source(self):
        if not self.voltage: 
            self.type="curent_source"; return "curent_source"
        else: 
            self.type="voltage_source"; return "voltage_source"

class AC_Source(SourceCurrent):...

class DC_Source(SourceCurrent):...
