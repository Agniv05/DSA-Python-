#  Depth-First Search (DFS) is an algorithm for traversing or searching through a graph or tree data structure. 
#  Unlike Breadth-First Search (BFS), which explores nodes level by level, DFS dives deep into one branch before 
#  backtracking to explore other branches. DFS can be implemented recursively or iteratively using a stack.

#  Recursive DFS Implementation in Python:
def dfs_recursive(graph, node, visited):
    # Add the current node to the visited set
    visited.add(node)
    print(node, end=" ")  # Print node to show the order of traversal

    # Recursively visit each unvisited neighbor
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Call DFS with an empty set for visited nodes
visited_nodes = set()
print("DFS Recursive Traversal Order:")
dfs_recursive(graph, "A", visited_nodes)
#  Output:
#  DFS Recursive Traversal Order:
#  A B D E F C


#  Recursive Traversal: Starting from the node, we mark it as visited, then recursively visit each neighbor that hasn’t been visited.
#  Tracking Visited Nodes: The visited set prevents re-visiting nodes and potential infinite loops.


#  Iterative DFS Implementation in Python:
def dfs_iterative(graph, start_node):
    # Stack to keep track of the nodes
    stack = [start_node]
    visited = set([start_node])
    dfs_order = []

    # Continue until stack is empty
    while stack:
        # Pop a node from the stack
        node = stack.pop()
        dfs_order.append(node)

        # Push all unvisited neighbors to the stack
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return dfs_order

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
print("DFS Iterative Traversal Order:", dfs_iterative(graph, start_node))
#  Output:
#  DFS Iterative Traversal Order: ['A', 'B', 'D', 'E', 'F', 'C']

#  Explicit Stack: The stack manages traversal order explicitly, pushing unvisited neighbors onto the stack.
#  Traversal Order: Nodes are explored in the order they’re popped from the stack.
