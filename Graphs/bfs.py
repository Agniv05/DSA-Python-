#  In Breadth-First Search, we start with a node (not necessarily the smallest or the largest)
#  and start exploring its connected nodes. The same process is repeated with all the connecting 
#  nodes until all the nodes are visited. We should first learn the concept of the BFS spanning 
#  tree in order to understand the Breadth-First Search in a very intuitive way.

from collections import deque

def bfs(graph, start_node):
    # Initialize a queue to manage nodes to visit and a list to track visited nodes
    queue = deque([start_node])
    visited = set([start_node])

    # List to store the order of visited nodes
    bfs_order = []

    while queue:
        # Pop the front of the queue
        node = queue.popleft()
        bfs_order.append(node)

        # Visit all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark neighbor as visited and add it to the queue
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

# Example usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start_node = "A"
print("BFS Traversal Order:", bfs(graph, start_node))
# BFS Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']



#  Applying the BFS using recursion:

def recursive_bfs(graph, queue, visited, bfs_order):
    # Base case: If the queue is empty, end recursion
    if not queue:
        return

    # Get the first node in the queue
    node = queue.pop(0)
    bfs_order.append(node)

    # Visit all neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    # Recursive call with updated queue
    recursive_bfs(graph, queue, visited, bfs_order)


# Wrapper function to initiate recursive BFS
def bfs(graph, start_node):
    # Initialize visited set and bfs_order list
    visited = set([start_node])
    bfs_order = []
    queue = [start_node]

    # Start the recursive BFS
    recursive_bfs(graph, queue, visited, bfs_order)
    return bfs_order


# Example usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start_node = "A"
print("Recursive BFS Traversal Order:", bfs(graph, start_node))
#Recursive BFS Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']
