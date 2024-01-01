# Define a Node class to represent individual elements in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the current node
        self.next = None  # Initialize the next pointer as None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the linked list as None

    # Method to append a new element to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new Node with the given data
        if not self.head:
            # If the linked list is empty, set the new node as the head
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the current node's data
            current = current.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the linked list

# Creating an instance of the LinkedList class
llist = LinkedList()

# Adding elements to the linked list using the append method
llist.append(1)
llist.append(2)
llist.append(3)

# Displaying the linked list
llist.display()
