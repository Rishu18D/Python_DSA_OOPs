# Input the array
arr = list(map(int, input("Enter your array (comma-separated values): ").split(',')))

# Input the value of k233
k = int(input("Enter the value of k: "))

# Check if k is valid
if k > len(arr) or k <= 0:
    print("Invalid value of k. Please enter a valid k.")
else:
    # Sort the array in descending order
    sorted_array = sorted(arr, reverse=True)

    # Print the k greatest elements
    print(f"The {k} greatest elements in the array are: {sorted_array[:k]}")
