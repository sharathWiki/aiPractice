from copy import deepcopy

def disp(a):
    i = 0
    while i < 9:
        print(a[i], " ", a[i + 1], " ", a[i + 2])
        i = i + 3
    print(" ")

def find(fa):
    fi = 0
    while fi < 9:
        if (fa[fi] == 0):
            return fi
        fi = fi + 1

def left(b):
    n = find(b)
    if n % 3 != 0:
        a = deepcopy(b)
        temp = a[n]
        a[n] = a[n - 1]
        a[n - 1] = temp
        return a
    else:
        return None

def right(b):
    n = find(b)
    if n % 3 != 2:
        a = deepcopy(b)
        temp = a[n]
        a[n] = a[n + 1]
        a[n + 1] = temp
        return a
    else:
        return None

def up(b):
    n = find(b)
    if n >= 3:
        a = deepcopy(b)
        temp = a[n]
        a[n] = a[n - 3]
        a[n - 3] = temp
        return a
    else:
        return None

def down(b):
    n = find(b)
    if n < 6:
        a = deepcopy(b)
        temp = a[n]
        a[n] = a[n + 3]
        a[n + 3] = temp
        return a
    else:
        return None

def heu(a, fin):
    h = 0
    for i in range(9):
        if a[i] != 0 and a[i] != fin[i]:
            h = h + 1
    return h

def astar(ini, fin):
    open_list = []
    closed_list = []
    open_list.append([ini, None, 0, heu(ini, fin)])  # [state, parent, g(n), h(n)]

    while open_list:
        open_list.sort(key=lambda x: x[2] + x[3])  # Sort based on f(n) = g(n) + h(n)
        current = open_list.pop(0)
        print(current)
        closed_list.append(current)

        if current[0] == fin:
            path = []
            while current[1] is not None:
                path.append(current[0])
                current = current[1]
            path.append(ini)
            path.reverse()
            return path

        moves = [left(current[0]), right(current[0]), up(current[0]), down(current[0])]
        for move in moves:
            if move is not None:
                if move not in [item[0] for item in open_list] and move not in [item[0] for item in closed_list]:
                    open_list.append([move, current, current[2] + 1, heu(move, fin)])
                else:
                    index_open = [item[0] for item in open_list].index(move) if move in [item[0] for item in open_list] else -1
                    index_closed = [item[0] for item in closed_list].index(move) if move in [item[0] for item in closed_list] else -1

                    if index_open != -1:
                        if open_list[index_open][2] > current[2] + 1:
                            open_list[index_open] = [move, current, current[2] + 1, heu(move, fin)]
                    elif index_closed != -1:
                        if closed_list[index_closed][2] > current[2] + 1:
                            closed_list[index_closed] = [move, current, current[2] + 1, heu(move, fin)]

    return None

ini = [2, 0, 3, 1, 8, 4, 7, 6, 5]
fin = [1, 2, 3, 8, 0, 4, 7, 6, 5]

path = astar(ini, fin)
if path is not None:
    print("Solution found:")
    for p in path:
        disp(p)
else:
    print("No solution found.")