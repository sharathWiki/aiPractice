import queue as q


def ucs(initial, goal, graph):
    pq = q.PriorityQueue()
    visited = set()

    pq.put((0, initial))
    while not pq.empty():
        cur = pq.get()
        curnode = cur[1][len(cur[1]) - 1]
        if curnode == goal:
            print('goal found')
            print(cur)
            break
        visited.add(cur[1])
        cost = cur[0]
        for i in graph[curnode]:
            if cur[1] + i not in visited:
                pq.put((cost + graph[curnode][i], cur[1] + i))


def main():
    graph = {'S': {'A': 1, 'B': 5, 'C': 15}, 'A': {'S': 1, 'G': 10}, 'B': {'S': 5, 'G': 5}, 'C': {'S': 15},
             'G': {'A': 10, 'B': 5, 'C': 5}}
    ucs('S', 'G', graph)


if __name__ == "__main__":
    main()
