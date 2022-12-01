# It is only possible iteratively

def breadth_first_traversal(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

graph = {
    'a' : ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f': [],
}

breadth_first_traversal(graph, 'a')