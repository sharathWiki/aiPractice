import copy


# class Stack:
#     def __init__(self):
#         self.data = []
#         self.top = -1
#
#     def push(self, val):
#         self.top += 1
#         self.data.append(val)
#
#     def pop(self):
#         if self.top == -1:
#             print("Stack is empty")
#             return None
#         else:
#             temp = self.data[self.top]
#             self.top -= 1
#             return temp
#
#     def empty(self):
#         return self.top == -1


class State:
    def __init__(self, blocks, actions=[]):
        self.blocks = blocks
        self.actions = actions

    def __str__(self):
        return str(self.blocks)

    def __eq__(self, other):
        self.blocks.sort(key = len)
        other.blocks.sort(key = len)
        # print(self.__str__(), other.__str__(), self.__str__() == other.__str__())
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(self.__str__())


def dfs(current, final, level, visited=set(), curlevel=0):
        if current == final:
            print(current.actions)
            print(current.blocks)
            return
        if level == curlevel:
            print(current.blocks)
            print("limit reached")
            return

        for i in range(len(current.blocks)):
            if len(current.blocks[i]) > 0:
                for j in range(len(current.blocks)):
                    if i == j:
                        continue
                    newbl = copy.deepcopy(current.blocks)
                    pick = newbl[i][-1]
                    del newbl[i][-1]
                    newbl[j].append(pick)
                    new = State(newbl, current.actions + [f"moved {pick} from {i} to {j} {newbl}"])
                    if new not in visited:
                        # print(new.blocks)
                        visited.add(new)
                        dfs(new, final, level, visited, curlevel+1)


if __name__ == '__main__':
    initial_state = State([[], [], ['A', 'B', 'C']])
    goal_state = State([[], [], ['C', 'A', 'B']])
    for i in range(1, 7):
        print(i)
        dfs(initial_state, goal_state, i)
