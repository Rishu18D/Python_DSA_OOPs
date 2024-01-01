class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create an instance of the Rectangle class
rectangle_area = Rectangle(324, 534)

# Call the area method and print the result
print("Area of rectangle =", rectangle_area.area())


            
            