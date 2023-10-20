from src.core.components_api_2 import Branch
from src.logic.add_nodes import add_node

def input_branch(circuit_init):
    node = tuple(input('укажите кортеж точек: ').split())
    slug = input('укажите название: ')
    x = int(input('укажите точку X: '))
    y = int(input('укажите точку Y: '))
    add_branch(node, x, y, slug, circuit_init)
    print(type(node), node) 

def add_branch(node, x, y, slug, circuit_init):
    branch = Branch(node, slug) 
    circuit_init.components_matrix_incidence[
        (
            add_node(x+10, y+10, node[0]), 
            add_node(x-10, y-10, node[1]),
        )
    ] = {f'{slug}' : branch}

