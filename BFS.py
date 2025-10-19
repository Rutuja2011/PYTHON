#slip5_1
#Write a program to implement Breadth Search First Search Traversal

graph = {
    '10': ['20', '30'],
    '20': ['40', '50'],
    '30': ['60', '70'],
    '40': [],
    '50': [],
    '60': [],
    '70': [],
}

def bfs(graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    print("Following is the Breadth-First Search:")

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Call the function
bfs(graph, '10')
