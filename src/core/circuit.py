class Ciruit:
    def __init__(self, list_branches = {}) -> None:
        """
        Circuit = [branch1, branch2, branch3, branch4,]\n
        branch  = {entry_node:(input, output), components:[]}
        
        """
        self.list_branches = list_branches

    def add_branch(self, branch):
        print("BRAAAAAAANCH", branch)
        self.list_branches.append(branch)

    def show_circuit(self):
        print(self.list_branches)
    
    def check_closed(self) -> bool:
        var = True
        return var