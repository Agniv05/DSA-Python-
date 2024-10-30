#  Stacks and Queues
#  Stacks (LIFO) and Queues (FIFO) are fundamental data structures with specific operations.

#  Stack (Last In First Out):

stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns the last element

#  Queue (First In First Out) using collections.deque:

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Removes and returns the first element


