import copy
import queue as q

class State:
    def __init__(self, board, heuristic=0, actions=[]):
        self.board = board
        self.actions = actions
        self.heuristic = heuristic
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
    #perfect score
    heur = 0
    for i in range(len(cur.board)):
        for j in range(len(cur.board[0])):
            if cur.board[i][j] != goal.board[i][j]:
                heur += 1
    return heur

def bfs(initial, final):
    queue = q.PriorityQueue()
    queue.put((calc_heuristic(initial, final), initial))
    visited = set()
    visited.add(initial)

    while not queue.empty():
        node = queue.get()
        state = node[1]
        heuristic = node[0]

        if heuristic == 0:
            print('soln found')
            print(state.actions)
            print(state.board)
            break

        if state.y > 0:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x], temp.board[temp.y-1][temp.x] = temp.board[temp.y-1][temp.x], temp.board[temp.y][temp.x]
            temp.y -= 1
            temp.actions.append("up")
            if temp not in visited:
                visited.add(temp)
                queue.put((calc_heuristic(temp, final), temp))

        if state.y < len(state.board) - 1:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x], temp.board[temp.y + 1][temp.x] = temp.board[temp.y + 1][temp.x], temp.board[temp.y][temp.x]
            temp.y += 1
            temp.actions.append("down")
            if temp not in visited:
                visited.add(temp)
                queue.put((calc_heuristic(temp, final), temp))

        if state.x > 0:
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x-1], temp.board[temp.y][temp.x] = temp.board[temp.y][temp.x], temp.board[temp.y][temp.x-1]
            temp.x -= 1
            temp.actions.append("left")
            if temp not in visited:
                visited.add(temp)
                queue.put((calc_heuristic(temp, final), temp))

        if state.x < len(state.board[0]):
            temp = copy.deepcopy(state)
            temp.board[temp.y][temp.x+1], temp.board[temp.y][temp.x] = temp.board[temp.y][temp.x], temp.board[temp.y][temp.x+1]
            temp.y -= 1
            temp.actions.append("right")
            if temp not in visited:
                visited.add(temp)
                queue.put((calc_heuristic(temp, final), temp))


if __name__ == "__main__":
    init = State([['2', '.', '3'], ['1', '8', '4'], ['7', '6', '5']])
    final = State([['1', '2', '3'], ['8', '.', '4'], ['7', '6', '5']])
    bfs(init, final)