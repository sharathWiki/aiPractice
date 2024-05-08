import copy

class State:
    def __init__(self, board, gn=0, heuristic=0, parent=None, actions=[]):
        self.board = board
        self.actions = actions
        self.gn = gn
        self.heuristic = heuristic
        self.parent = parent
        self.x, self.y = self.find()

    def __str__(self):
        return str(self.board)

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def find(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '.':
                    return j, i


#number of misplaced tiles
def calc_heuristic(cur, goal):
    #min score
    heur = 0
    for i in range(len(cur.board)):
        for j in range(len(cur.board[0])):
            if cur.board[i][j] == goal.board[i][j]:
                heur += 1
    return heur

def astar(initial, final):
    queue: list[State] = [initial]
    visited = [init]

    while len(queue) > 0:
        state = queue.pop(0)

        if state.heuristic == 9:
            print('soln found')
            print(state.actions)
            stk = []
            while state != None:
                stk.append(state)
                state = state.parent
            while (len(stk) > 0):
                top = stk.pop()
                print(top.board, top.gn + top.heuristic)
            break

        if state.y > 0:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x], temp.board[temp.y-1][temp.x] = temp.board[temp.y-1][temp.x], temp.board[temp.y][temp.x]
            temp.y -= 1
            temp.actions.append("up")
            temp.parent = state
            temp.heuristic = calc_heuristic(temp, final)
            temp.gn = state.gn - 1
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)
            else:
                for i in range(len(visited)):
                    if visited[i] == temp and visited[i].gn < temp.gn:
                        visited[i].gn = temp.gn
                        visited[i].parent = temp.parent


        if state.y < len(state.board) - 1:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x], temp.board[temp.y + 1][temp.x] = temp.board[temp.y + 1][temp.x], temp.board[temp.y][temp.x]
            temp.y += 1
            temp.actions.append("down")
            temp.parent = state
            temp.heuristic = calc_heuristic(temp, final)
            temp.gn = state.gn - 1
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)
            else:
                for i in range(len(visited)):
                    if visited[i] == temp and visited[i].gn < temp.gn:
                        visited[i].gn = temp.gn
                        visited[i].parent = temp.parent

        if state.x > 0:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x-1], temp.board[temp.y][temp.x] = temp.board[temp.y][temp.x], temp.board[temp.y][temp.x-1]
            temp.x -= 1
            temp.actions.append("left")
            temp.parent = state
            temp.heuristic = calc_heuristic(temp, final)
            temp.gn = state.gn - 1
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)
            else:
                for i in range(len(visited)):
                    if visited[i] == temp and visited[i].gn < temp.gn:
                        visited[i].gn = temp.gn
                        visited[i].parent = temp.parent

        if state.x < len(state.board[0]):
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x+1], temp.board[temp.y][temp.x] = temp.board[temp.y][temp.x], temp.board[temp.y][temp.x+1]
            temp.y -= 1
            temp.actions.append("right")
            temp.parent = state
            temp.heuristic = calc_heuristic(temp, final)
            temp.gn = state.gn - 1
            if temp not in visited:
                visited.append(temp)
                queue.append(temp)
            else:
                for i in range(len(visited)):
                    if visited[i] == temp and visited[i].gn < temp.gn:
                        visited[i].gn = temp.gn
                        visited[i].parent = temp.parent

        queue.sort(key=lambda x: x.gn + x.heuristic, reverse=True)

if __name__ == "__main__":
    init = State([['2', '.', '3'], ['1', '8', '4'], ['7', '6', '5']])
    final = State([['1', '2', '3'], ['8', '.', '4'], ['7', '6', '5']])
    astar(init, final)