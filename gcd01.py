    # Program to calculate GCD or HCF of numbers in a list

# Function to calculate GCD of two numbers
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input: Length of the list
n = int(input("Length of the list: "))

# Initialize an empty list to store elements
num_list = []

# Input: Elements of the list
for i in range(n):
    element = int(input("Enter an element: "))
    num_list.append(element)

# Initialize GCD to the first element of the list
gcd_result = num_list[0]

# Calculate GCD of all elements in the list
for num in num_list[1:]:
    gcd_result = calculate_gcd(gcd_result, num)

# Print the GCD
print("GCD of the numbers in the list is:", gcd_result)
