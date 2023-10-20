import json


def save_circuit(circuit):
    """
    {
        components : {
                1 : {res obj},
                2 : {nod obj},
                3 : {cap obj},
                4 : {cur obj},
                 ...
                n : {nnn obj},

        },
        connetion : {
            1 : [2, 3, 4],
            2 : [1, 3, 4],
            3 : [1, 2, 4],
             ...
            n : [x, y, z],
        },
    }


    """
    with open(f'{circuit.name_circuit}.json', 'w') as outfile:
        
        serializer_data = {}

        serializer_data['components'] = circuit.components_matrix_incidence
        serializer_data['connections'] = circuit.components_matrix_adjacency

        json.dump(serializer_data, outfile)

def open_circuit(file_name, circuit):
    with open(f'{file_name}') as json_file:
        open_dict = json.load(json_file)
        circuit.components_matrix_incidence = open_dict['components']
        circuit.components_matrix_adjacency = open_dict['connections']
        json_file.close()

