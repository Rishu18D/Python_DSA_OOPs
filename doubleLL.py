# Define a Node class to represent individual elements in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Define a DoublyLinkedList class to manage the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the doubly linked list as None

    # Method to append a new element to the end of the doubly linked list
    def append(self, data):
        new_node = Node(data)  # Create a new Node with the given data
        if not self.head:
            # If the doubly linked list is empty, set the new node as the head
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current  # Set the previous pointer of the new node

    # Method to display the elements in the doubly linked list in both forward and backward directions
    def display(self):
        current = self.head

        # Forward traversal
        print("Forward:")
        while current:
            print(current.data, end=" <-> ")  # Print the current node's data
            current = current.next  # Move to the next node
        print("None")

        # Backward traversal
        print("Backward:")
        while current:
            print(current.data, end=" <-> ")  # Print the current node's data
            current = current.prev  # Move to the previous node
        print("None")

# Creating an instance of the DoublyLinkedList class
dllist = DoublyLinkedList()

# Adding elements to the doubly linked list using the append method
dllist.append(1)
dllist.append(2)
dllist.append(3)

# Displaying the doubly linked list in both forward and backward directions
dllist.display()
