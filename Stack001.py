#Stack data structure...
class Stack:
    def __init__(self):
        self.items = []
def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

input_string = "Hello, World!"
reversed = reverse_string(input_string)
print(reversed)  # This will print "!dlroW ,olleH"

