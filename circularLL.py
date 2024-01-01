# Define a Node class to represent individual elements in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

# Define a CircularLinkedList class to manage the circular linked list
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the circular linked list as None

    # Method to append a new element to the end of the circular linked list
    def append(self, data):
        new_node = Node(data)  # Create a new Node with the given data
        if not self.head:
            # If the circular linked list is empty, set the new node as the head
            self.head = new_node
            new_node.next = self.head  # Make the new node point to itself to form a circular reference
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node  # Set the last node's next pointer to the new node
            new_node.next = self.head  # Make the new node point to the head to form a circular reference

    # Method to display the elements in the circular linked list
    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")  # Print the current node's data
            current = current.next  # Move to the next node
            if current == self.head:
                break  # Exit the loop when we reach the head again
        print("Head")

# Creating an instance of the CircularLinkedList class
cllist = CircularLinkedList()

# Adding elements to the circular linked list using the append method
cllist.append(1)
cllist.append(2)
cllist.append(3)

# Displaying the circular linked list
cllist.display()
