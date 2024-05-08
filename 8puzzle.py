import copy
# start current in g
# currrent end in heuristic
# save f in enqueue as wee
q=[]
visited=[]

def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return ([i,j])


#f(n)=g(n)+h(n)
def heuristic(s, g):
    return heuristic_h(s, g)

#g(n)
# def heuristic_g(parent_g, transition_cost):
#     return parent_g + transition_cost

#h(n)
def heuristic_h(s,g):
    d=0
    for i in range(3):
        for j in range(3):
            if s[i][j]!=g[i][j]:
                d+=1
    return d
def enqueue(s, g_val, h_val):
    global q
    f_val = g_val + h_val
    q.append((f_val, s))
    q.sort(key=lambda x: x[0])

def dequeue():
    global q
    if len(q) > 0:
        return q.pop(0)[1]
    else:
        return None

#UP MOVEMENT
def up(s,pos):
    i=pos[0]
    j=pos[1]

    if i>0:
        temp=copy.deepcopy(s)
        temp[i][j]=temp[i-1][j]
        temp[i-1][j]=0
        return temp
    else:
        return(s)

#UP MOVEMENT
def down(s, pos):
    i = pos[0]
    j = pos[1]

    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return temp
    else:
        return (s)

#LEFT MOVEMENT
def left(s, pos):
    i = pos[0]
    j = pos[1]

    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return(temp)
    else:
        return (s)

#RIGHT MOVEMENT
def right(s, pos):
    i = pos[0]
    j = pos[1]

    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return temp
    else:
        return (s)


def search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return

    # Initialize visited here before it's referenced
    visited = [s]

    global q
    while True:
        pos = find_pos(curr_state)
        # MOVE UP
        new = up(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Found")
                print(visited + [g])
                return
        else:
            if new not in visited:
                enqueue(new, heuristic(curr_state, g), heuristic(new, g))  # Updated this line

        # MOVE DOWN
        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Found")
                print(visited + [g])
                return
        else:
            if new not in visited:
                enqueue(new, heuristic(curr_state, g), heuristic(new, g))  # Updated this line

        # MOVE LEFT
        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Found")
                print(visited + [g])
                return
        else:
            if new not in visited:
                enqueue(new, heuristic(curr_state, g), heuristic(new, g))  # Updated this line

        # MOVE RIGHT
        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Found")
                print(visited + [g])
                return
        else:
            if new not in visited:
                enqueue(new, heuristic(curr_state, g), heuristic(new, g))  # Updated this line

        visited.append(curr_state)
        # Last position
        if len(q) > 0:
            curr_state = dequeue(g)
        else:
            print("not found")
            return


def main():
    s = [[2,0,3], [1,8,4], [7,6,5]]
    g = [[1,2,3], [8,0,4], [7,6,5]]
    global q
    global visited
    q=q
    visited=visited+[s]
    search(s,g)

if __name__ == "__main__":
    main()
