from .circuit_components import Component

class Circuit:
    def __init__(self, components_list) -> None:
        self.components = []
        for component in components_list:
            self.components.append(Component(component))

        self.nodes = []
        for component in self.components:
            if component.terminal1 not in self.nodes:
                self.nodes.append(component.terminal1)
            if component.terminal2 not in self.nodes:
                self.nodes.append(component.terminal2)