#    Linked Lists addresses few of the limitations of the arrays. Example:

#    1. insertion or deletion in case of an array is expEnsive(complex position-based)
#    2. as arrays are static structures, they cannot be easily extended or reduced
#    3. fixed size
#    4. one block allocation

#    Linked list---> A LINEAR DYNAMIC DATA STRUCTURE.
#    consists of nodes
#    the nodes consist of the data and the reference(POINTERS) to the next node
#    th last node(THE FINAL ELEMENT) has a reference to null
#    the head(entry point into a linked list) is not a node but a REFERENCE TO THE FIRST NODE
#    if the list is empty, the head is a null reference
#    the size of the list can change during program execution
#    it can be made as long as necessary, until memory is depleted
#    it avoids wastage of memory space but additional memory is required for pointers
#    
#    NOTE:A null reference, also known as a null pointer, is a reference or pointer that does not point to a valid object or memory location. In other words, it is a reference that has no value or points to nothing.
#    LINKED LIST IS AN ABSTRACT DATA TYPE
#    ARRAYS--->simple and easy to use and takes constant time for accessing elements based on indices as it is random access O(1)(takes one multiplication and addition, both of which take a constant time)
#    DYNAMIC ARRAYS--->random access, variable-size list data structure that allows elements to be added or removed.
#    LINKED LIST--->takes O(n) to access the elements
#    ----COMPARATIVE STUDY----
#    Contiguous memory allocation: Dynamic arrays store elements in contiguous blocks of memory, which means that each element is stored next to the previous one in memory.
#    Fixed-size elements: Dynamic arrays typically store elements of a fixed size, which makes it easy to calculate the memory address of each element.
#    Random access: Dynamic arrays allow for random access to elements, meaning that you can access any element directly using its index.
#    Cache-friendly: Dynamic arrays are cache-friendly, meaning that the CPU can efficiently access elements in the array because they are stored in contiguous memory locations.
#    Resizing: Dynamic arrays can be resized by allocating a new block of memory and copying the elements from the old block to the new block.


#SINGLY LINKED LIST:
# 1. Structure for linked list node
class Node:
    # Aim: Initialize a new node with data and a pointer to the next node
    def __init__(self, data):
        self.data = data
        self.next = None


# 2. Function to create a new node
def create_node(data):
    # Aim: Create a new node with the given data
    return Node(data)


# 3. Function to insert node at beginning
def insert_at_beginning(head, data):
    # Aim: Insert a new node with the given data at the beginning of the linked list
    new_node = create_node(data)
    new_node.next = head
    return new_node  # New head of the list


# 4. Function to insert node at end
def insert_at_end(head, data):
    # Aim: Insert a new node with the given data at the end of the linked list
    new_node = create_node(data)
    if not head:
        return new_node  # New node becomes the head if list is empty
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


# 5. Function to reverse linked list
def reverse_linked_list(head):
    # Aim: Reverse the linked list
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # New head of the reversed list


# 6. Function to insert node at particular position
def insert_at_position(head, data, position):
    # Aim: Insert a new node with the given data at the specified position
    if position == 0:
        return insert_at_beginning(head, data)
    new_node = create_node(data)
    current = head
    for _ in range(position - 1):
        if not current:
            raise IndexError("Position out of bounds")
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head


# 7. Function to create linked list from a list of elements
def create_linked_list(elements):
    # Aim: Create a linked list from a list of elements
    head = None
    for element in elements:
        head = insert_at_end(head, element)
    return head


# 8. Function to delete first node
def delete_first_node(head):
    # Aim: Delete the first node in the linked list
    if not head:
        return None
    return head.next  # New head of the list


# 9. Function to delete last node
def delete_last_node(head):
    # Aim: Delete the last node in the linked list
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


# 10. Function to delete node at nth position
def delete_node_at_position(head, position):
    # Aim: Delete the node at the specified position
    if position == 0:
        return delete_first_node(head)
    current = head
    for _ in range(position - 1):
        if not current.next:
            raise IndexError("Position out of bounds")
        current = current.next
    if not current.next:
        raise IndexError("Position out of bounds")
    current.next = current.next.next
    return head


# Helper function to print the linked list (for testing purposes)
def print_linked_list(head):
    # Aim: Print all nodes in the linked list
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")



#DOUBLY LINKED LIST:
# 1. Structure for doubly linked list node
class Node:
    # Aim: Initialize a new node with data, and pointers to the previous and next nodes
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# 2. Function to create a new node
def create_node(data):
    # Aim: Create a new node with the given data
    return Node(data)


# 3. Function to insert node at beginning
def insert_at_beginning(head, data):
    # Aim: Insert a new node with the given data at the beginning of the doubly linked list
    new_node = create_node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node  # New head of the list


# 4. Function to insert node at end
def insert_at_end(head, data):
    # Aim: Insert a new node with the given data at the end of the doubly linked list
    new_node = create_node(data)
    if not head:
        return new_node  # New node becomes the head if list is empty
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head


# 5. Function to reverse doubly linked list
def reverse_linked_list(head):
    # Aim: Reverse the doubly linked list
    current = head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node
    return prev  # New head of the reversed list


# 6. Function to insert node at particular position
def insert_at_position(head, data, position):
    # Aim: Insert a new node with the given data at the specified position
    if position == 0:
        return insert_at_beginning(head, data)
    new_node = create_node(data)
    current = head
    for _ in range(position - 1):
        if not current:
            raise IndexError("Position out of bounds")
        current = current.next
    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    return head


# 7. Function to create doubly linked list from a list of elements
def create_linked_list(elements):
    # Aim: Create a doubly linked list from a list of elements
    head = None
    for element in elements:
        head = insert_at_end(head, element)
    return head


# 8. Function to delete first node
def delete_first_node(head):
    # Aim: Delete the first node in the doubly linked list
    if not head:
        return None
    if not head.next:
        return None  # List becomes empty
    head = head.next
    head.prev = None
    return head


# 9. Function to delete last node
def delete_last_node(head):
    # Aim: Delete the last node in the doubly linked list
    if not head or not head.next:
        return None
    current = head
    while current.next:
        current = current.next
    current.prev.next = None
    return head


# 10. Function to delete node at nth position
def delete_node_at_position(head, position):
    # Aim: Delete the node at the specified position
    if position == 0:
        return delete_first_node(head)
    current = head
    for _ in range(position):
        if not current:
            raise IndexError("Position out of bounds")
        current = current.next
    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
    return head


# Helper function to print the doubly linked list (for testing purposes)
def print_linked_list(head):
    # Aim: Print all nodes in the doubly linked list
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")



#CIRCULAR LINKED LIST:
# 1. Structure for circular linked list node
class Node:
    # Aim: Initialize a new node with data and a pointer to the next node
    def __init__(self, data):
        self.data = data
        self.next = None


# 2. Function to create a new node
def create_node(data):
    # Aim: Create a new node with the given data
    return Node(data)


# 3. Function to insert node at beginning
def insert_at_beginning(head, data):
    # Aim: Insert a new node with the given data at the beginning of the circular linked list
    new_node = create_node(data)
    if not head:
        new_node.next = new_node  # Point to itself if it's the only node
        return new_node  # New head of the list
    current = head
    while current.next != head:
        current = current.next  # Traverse to the last node
    current.next = new_node  # Point last node to new node
    new_node.next = head  # New node points to the old head
    return new_node  # New head of the list


# 4. Function to insert node at end
def insert_at_end(head, data):
    # Aim: Insert a new node with the given data at the end of the circular linked list
    new_node = create_node(data)
    if not head:
        new_node.next = new_node  # Point to itself if it's the only node
        return new_node  # New head of the list
    current = head
    while current.next != head:
        current = current.next  # Traverse to the last node
    current.next = new_node  # Point last node to new node
    new_node.next = head  # New node points to head
    return head


# 5. Function to reverse circular linked list
def reverse_linked_list(head):
    # Aim: Reverse the circular linked list
    if not head or head.next == head:
        return head  # No change if list is empty or has one node
    prev = None
    current = head
    first = head
    while True:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        if current == first:
            break
    head.next = prev  # Connect old head to new head
    return prev  # New head of the reversed list


# 6. Function to insert node at particular position
def insert_at_position(head, data, position):
    # Aim: Insert a new node with the given data at the specified position
    if position == 0:
        return insert_at_beginning(head, data)
    new_node = create_node(data)
    current = head
    for _ in range(position - 1):
        current = current.next
        if current == head:
            raise IndexError("Position out of bounds")
    new_node.next = current.next
    current.next = new_node
    return head


# 7. Function to create circular linked list from a list of elements
def create_linked_list(elements):
    # Aim: Create a circular linked list from a list of elements
    head = None
    for element in elements:
        head = insert_at_end(head, element)
    return head


# 8. Function to delete first node
def delete_first_node(head):
    # Aim: Delete the first node in the circular linked list
    if not head:
        return None  # Empty list
    if head.next == head:
        return None  # List becomes empty after deletion
    current = head
    while current.next != head:
        current = current.next  # Traverse to the last node
    current.next = head.next  # Last node points to the second node
    return head.next  # New head of the list


# 9. Function to delete last node
def delete_last_node(head):
    # Aim: Delete the last node in the circular linked list
    if not head:
        return None  # Empty list
    if head.next == head:
        return None  # List becomes empty after deletion
    current = head
    while current.next.next != head:
        current = current.next  # Traverse to the second last node
    current.next = head  # Point to head, effectively removing the last node
    return head


# 10. Function to delete node at nth position
def delete_node_at_position(head, position):
    # Aim: Delete the node at the specified position
    if position == 0:
        return delete_first_node(head)
    current = head
    for _ in range(position - 1):
        current = current.next
        if current == head:
            raise IndexError("Position out of bounds")
    if current.next == head:
        return head  # Nothing to delete if we're at the last node
    current.next = current.next.next  # Skip the node to be deleted
    return head


# Helper function to print the circular linked list (for testing purposes)
def print_linked_list(head):
    # Aim: Print all nodes in the circular linked list
    if not head:
        print("List is empty.")
        return
    current = head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")







# Circular Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def create_node(data):
    return Node(data)

# Insert node at the beginning of the circular doubly linked list
def insert_at_beginning(head, data):
    new_node = create_node(data)
    if not head:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    tail = head.prev
    new_node.next = head
    new_node.prev = tail
    tail.next = new_node
    head.prev = new_node
    return new_node

# Insert node at the end of the circular doubly linked list
def insert_at_end(head, data):
    new_node = create_node(data)
    if not head:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    tail = head.prev
    tail.next = new_node
    new_node.prev = tail
    new_node.next = head
    head.prev = new_node
    return head

# Insert node at a specific position in the circular doubly linked list
def insert_at_position(head, data, position):
    new_node = create_node(data)
    if not head:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    if position == 1:
        return insert_at_beginning(head, data)
    current = head
    for _ in range(position - 2):
        current = current.next
        if current == head:
            raise IndexError("Position out of range")
    new_node.next = current.next
    new_node.prev = current
    current.next.prev = new_node
    current.next = new_node
    return head

# Delete the first node of the circular doubly linked list
def del_at_beginning(head):
    if not head:
        return None
    if head.next == head:
        return None  # Only one element
    tail = head.prev
    new_head = head.next
    tail.next = new_head
    new_head.prev = tail
    return new_head

# Delete the last node of the circular doubly linked list
def del_at_end(head):
    if not head:
        return None
    if head.next == head:
        return None  # Only one element
    tail = head.prev
    new_tail = tail.prev
    new_tail.next = head
    head.prev = new_tail
    return head

# Reverse the circular doubly linked list
def reverse(head):
    if not head or head.next == head:
        return head  # No change if list is empty or has one node
    current = head
    prev = None
    while True:
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node
        if current == head:
            break
    head.next = prev
    prev.prev = head
    return prev  # New head of the reversed list

# Display the circular doubly linked list
def display(head):
    if not head:
        print("List is empty")
        return
    current = head
    while True:
        print(current.data, end=" <-> ")
        current = current.next
        if current == head:
            break
    print("Head")

# Example usage
head = None
head = insert_at_beginning(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)
head = insert_at_position(head, 15, 2)
print("List after insertions:")
display(head)

head = del_at_beginning(head)
print("List after deleting the first node:")
display(head)

head = del_at_end(head)
print("List after deleting the last node:")
display(head)

head = reverse(head)
print("List after reversal:")
display(head)
