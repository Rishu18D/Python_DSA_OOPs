# Function to create a rectangle pattern
def create_rectangle(pattern, num):
    for _ in range(num):
        print(pattern * num)

# Function to create a triangle pattern
def create_triangle(pattern, num):
    for i in range(1, num + 1):
        print(pattern * i)

# Function to create a diamond pattern
def create_diamond(pattern, num):
    for i in range(1, num + 1):
        print(" " * (num - i) + pattern * (2 * i - 1))
    for i in range(num - 1, 0, -1):
        print(" " * (num - i) + pattern * (2 * i - 1))

# Function to create a pyramid pattern
def create_pyramid(pattern, num):
    for i in range(1, num + 1):
        print(" " * (num - i) + pattern * (2 * i - 1))
# Function to create a right-angled triangle pattern
def create_right_triangle(pattern, num):
    for i in range(1, num + 1):
        print(pattern * i)

# Function to create a hollow square pattern
def create_hollow_square(pattern, num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print(pattern * num)
        else:
            print(pattern + " " * (num - 2) + pattern)
        

# Main program
Shape_request = input("Enter a shape (Rectangle, Triangle, Diamond, Pyramid, RightTriangle, HollowSquare): ")
Pattern_design = input("Enter your design character: ")
num = int(input("Enter the size of the shape: "))

if Shape_request == "Rectangle":
    create_rectangle(Pattern_design, num)
elif Shape_request == "Triangle":
    create_triangle(Pattern_design, num)
elif Shape_request == "Diamond":
    create_diamond(Pattern_design, num)
elif Shape_request == "Pyramid":
    create_pyramid(Pattern_design, num)
elif Shape_request == "RightTriangle":
    create_right_triangle(Pattern_design, num)
elif Shape_request == "HollowSquare":
    create_hollow_square(Pattern_design, num)    
else:
 print("Invalid shape request. Please enter one of the following: Rectangle, Triangle, Diamond, Pyramid, RightTriangle, HollowSquare")
