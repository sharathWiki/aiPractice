import queue as Q

def search(graph, start, end):
    queue = Q.PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            print("path found")
            print(str(node[1]))
            print("cost = ", node[0])
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = list(node[1])
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

def main():
    graph = {'S': {'A': 1, 'B': 5, 'C': 15}, 'A': {'S': 1, 'G': 10}, 'B': {'S': 5, 'G': 5}, 'C': {'S': 15}, 'G': {'A': 10, 'B': 5, 'C': 5}}
    search(graph, 'S', 'G')

if __name__ == "__main__":
    main()
