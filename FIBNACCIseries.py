# Function to generate the Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Generate and print the Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = fibonacci(num_terms)
    print("Fibonacci Sequence:")
    print(fib_sequence)
