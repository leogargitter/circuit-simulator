class Component:
    def __init__(self, component_string) -> None:
        
        component_values = component_string.split(":")
        self.type = component_values[0]
        
        terminal_values = component_values[1].split(" ")
        self.name = terminal_values[0]
        self.terminal1 = terminal_values[1]
        self.terminal2 = terminal_values[2]
        
        component_parameters = component_values[1].split('"')
        
        if self.type == "R":
            self.r = component_parameters[1].split(" ")[0]
            self.r_unit = component_parameters[1].split(" ")[1]
            
        if self.type == "C":
            self.c = component_parameters[1].split(" ")[0]
            self.c_unit = component_parameters[1].split(" ")[1]
        
        if self.type == "L":
            self.l = component_parameters[1].split(" ")[0]
            self.l_unit = component_parameters[1].split(" ")[1]
        
        if self.type == "Diode":
            self.i_s = component_parameters[1].split(" ")[0]
            self.i_s_unit = component_parameters[1].split(" ")[1]
            
            self.v_j = component_parameters[9].split(" ")[0]
            self.v_j_unit = component_parameters[9].split(" ")[1]
            
        if self.type == "Vdc":
            self.v = component_parameters[1].split(" ")[0]
            self.v_unit = component_parameters[1].split(" ")[1]
        