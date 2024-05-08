import copy
import queue as q

class State:
    def __init__(self, blocks, actions=[]):
        self.blocks = blocks
        self.actions = actions

    def __str__(self):
        return str(self.blocks)

    def __eq__(self, other):
        self.blocks.sort(key=len)
        other.blocks.sort(key=len)
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(self.__str__())


def bfs(initial, final):
    visited = set()
    queue = q.Queue()
    queue.put(initial)

    while not queue.empty():
        node = queue.get()
        visited.add(node)

        if node == final:
            print(node.actions)
            print(node.blocks)
            break

        for i in range(len(node.blocks)):
            if len(node.blocks[i]) > 0:
                for j in range(len(node.blocks)):
                    if i == j:
                        continue
                    newbl = copy.deepcopy(node.blocks)
                    pick = newbl[i][-1]
                    del newbl[i][-1]
                    newbl[j].append(pick)
                    new = State(newbl, node.actions + [f"moved {pick} from {i} to {j} {node.__str__()}"])
                    if new not in visited:
                        queue.put(new)


if __name__ == '__main__':
    initial_state = State([[], [], ['A', 'B', 'C']])
    goal_state = State([[], [], ['C', 'A', 'B']])
    bfs(initial_state, goal_state)
