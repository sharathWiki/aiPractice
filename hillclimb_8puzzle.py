# simple hill climb only
import copy

class State:
    def __init__(self, board, heuristic=0, actions=[]):
        self.board = board
        self.heuristic = heuristic
        self.actions = actions
        self.x, self.y = self.find()

    def find(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '.':
                    return j, i
                
    def __str__(self) -> str:
        return str(self.board)
    
    def __hash__(self) -> int:
        return hash(self.__str__())

    def __eq__(self, value) -> bool:
        return self.__str__() == value.__str__()
    
def heuristic(state, goal):
    score = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != goal[i][j]:
                score += 1

    return score

def HillClimb(init: State, final: State):
    visited = set()

    while True:
        if init == final:
            print('found')
            print(init.actions)
            print(init.board)
            break
        if init.x > 0:
            newboard = copy.deepcopy(init.board)
            newboard[init.y][init.x], newboard[init.y][init.x-1] = newboard[init.y][init.x-1], newboard[init.y][init.x]
            h = heuristic(newboard, final.board)
            new = State(newboard, heuristic(newboard, final.board), init.actions + ["Left"])
            if h < init.heuristic:
                if new not in visited:
                    visited.add(new)
                    init = new
                    continue
                else:
                    print('found in visited')
                    break
            else:
                pass
        
        if init.x < len(init.board[0]) - 1:
            newboard = copy.deepcopy(init.board)
            newboard[init.y][init.x], newboard[init.y][init.x+1] = newboard[init.y][init.x+1], newboard[init.y][init.x]
            h = heuristic(newboard, final.board)
            new = State(newboard, heuristic(newboard, final.board), init.actions + ["Right"])
            if h < init.heuristic:
                if new not in visited:
                    visited.add(new)
                    init = new
                    continue
                else:
                    print('found in visited')
                    break
            else:
                pass
        
        if init.y > 0:
            newboard = copy.deepcopy(init.board)
            newboard[init.y-1][init.x], newboard[init.y][init.x] = newboard[init.y][init.x], newboard[init.y-1][init.x]
            h = heuristic(newboard, final.board)
            new = State(newboard, heuristic(newboard, final.board), init.actions + ["Up"])
            if h < init.heuristic:
                if new not in visited:
                    visited.add(new)
                    init = new
                    continue
                else:
                    print('found in visited')
                    break
            else:
                pass

        if init.y < len(init.board) + 1:
            newboard = copy.deepcopy(init.board)
            newboard[init.y][init.x], newboard[init.y+1][init.x] = newboard[init.y+1][init.x], newboard[init.y][init.x]
            h = heuristic(newboard, final.board)
            new = State(newboard, heuristic(newboard, final.board), init.actions + ["Down"])
            if h < init.heuristic:
                if new not in visited:
                    visited.add(new)
                    init = new
                    continue
                else:
                    print('found in visited')
                    break
            else:
                pass

if __name__ == "__main__":
    init = State([['2', '.', '3'], ['1', '8', '4'], ['7', '6', '5']])
    final = State([['1', '2', '3'], ['8', '.', '4'], ['7', '6', '5']])
    init.heuristic = heuristic(init.board, final.board)
    HillClimb(init, final)