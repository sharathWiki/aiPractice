class Node:
    def __init__(self, andNodes, orNodes, cost, val, parent=None) -> None:
        self.andNodes: list[Node] = andNodes
        self.orNodes: list[Node] = orNodes
        self.cost: int = cost
        self.val = val
        self.parent: Node = parent

    def add_child(self, cost, val, type):
        if type == "and":
            self.andNodes.append(Node([], [], cost, val, self))
        else:
            self.orNodes.append(Node([], [], cost, val, self))

    def __str__(self) -> str:
        return str(self.val)
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()
    
    def __hash__(self) -> int:
        return hash(self.__str__())

    def calc_cost(self):
        andcost = sum([x.calc_cost() for x in self.andNodes])
        orcost = [x.calc_cost() for x in self.orNodes]
        
        if andcost == 0 and len(orcost) == 0:
            pass
        else:
            self.cost = min(min(orcost), andcost) if len(orcost) > 0 else andcost
        return self.cost

if __name__ == "__main__":
    b = Node([], [], 6, 'B')
    b.add_child(5, 'G', "or")
    b.add_child(7, 'H', "or")
    d = Node([], [], 10, 'D')
    d.add_child(4, 'E', "and")
    d.add_child(4, 'F', "and")
    root = Node([b], [d], 0, 'A')
    root.add_child(12, 'C', "and")
    print(root.calc_cost())