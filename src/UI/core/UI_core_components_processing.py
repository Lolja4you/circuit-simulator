from .UI_core_draw_components import DrawNode, DrawResisrtor, DrawWire, DrawCapacitor, DrawSource, DrawInductor

# components_dict = {
#     # 1 : {
#     #      'type': 'wire', 
#     #      'x': 250, 'y':250, 
#     #      'length': 100, 
#     #      'angle': 0, 
#     #      'color':'white'
#     #     },
#     # 2 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 90, 'color':'white'},
#     # 3 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 180, 'color':'white'},
#     # 4 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 270, 'color':'white'},
#     # 5 : {'type': 'wire', 'x': 900, 'y':800, 'length': 100, 'angle': 30, 'color':'white'},
#     # 6 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 45, 'color':'white'},
#     # 7 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 60, 'color':'white'},
#     8 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 75, 'color':'white'},
#     # 9 : {'type': 'wire', 'x': 250, 'y':250, 'length': 100, 'angle': 15, 'color':'white'},
#     # 10 : {'type': 'wire', 'x': 347, 'y':224, 'length': 100, 'angle': 15, 'color':'white'},
#     11 : {'type': 'node', 'x': 600, 'y':700, 'length': 0, 'angle': 0, 'color':'red'},
#     12 : {'type': 'node', 'x': 600, 'y':700, 'length': 0, 'angle': 0, 'color':'white'},
#     13 : {'type': 'resistor', 'x': 650, 'y':200, 'length': 100, 'angle': 0, 'color':'white'},
#     15 : {'type': 'resistor', 'x': 200, 'y':400, 'length': 100, 'angle': 90, 'color':'white'},
#     16 : {'type': 'node', 'x': 0, 'y':0, 'length': 0, 'angle': 0, 'color':'white'},
#     17 : {'type': 'node', 'x': 600, 'y':300, 'length': 0, 'angle': 0, 'color':'white'},
#     18 : {'type': 'resistor', 'x': 250, 'y':400, 'length': 100, 'angle': 30, 'color':'white'},
# }


def components_drawer(canvas, ciruit):
    components_dict = ciruit.components_matrix_incidence
    components = []
    for component in components_dict:
        try:
            component_type = components_dict[component]['type']
        except KeyError: component_type = 'unkown'

        if 'node' in component_type:
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle']
            color = components_dict[component]['color']
            components.append(DrawNode(canvas, x=x, y=y, length=length, angle=angle, color=color))

        elif 'wire' in component_type:
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle']
            color = components_dict[component]['color']
            components.append(DrawWire(canvas, x=x, y=y, length=length, angle=angle, color=color))

        elif 'resistor' in component_type:
            print(component)
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle']
            color = components_dict[component]['color']
            components.append(DrawResisrtor(canvas, x=x, y=y, pk=int(component), length=length, angle=angle, color=color, ciruit=ciruit))

        elif 'capacitor' in component_type:
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle']
            color = components_dict[component]['color']
            components.append(DrawCapacitor(canvas, x=x, y=y, pk=int(component), length=length, angle=angle, color=color, ciruit=ciruit))
        elif 'source' in component_type:
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle'] 
            color = components_dict[component]['color']
            components.append(DrawSource(canvas, x=x, y=y, pk=int(component), length=length, angle=angle, color=color, ciruit=ciruit))
        elif 'inductor' in component_type:
            x = components_dict[component]['x']
            y = components_dict[component]['y']
            length = components_dict[component]['length']
            angle = components_dict[component]['angle'] 
            color = components_dict[component]['color']
            components.append(DrawInductor(canvas, x=x, y=y, pk=int(component), length=length, angle=angle, color=color, ciruit=ciruit))
        elif 'unkown' in component_type: continue
    

    return components