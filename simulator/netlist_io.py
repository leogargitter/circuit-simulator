
def read_netlist(path_to_netlist):
    with open(path_to_netlist, 'r') as file:
        return file.readlines()[2:]