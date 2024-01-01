def fibonacci(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Example usage:
n = 10
result = fibonacci(n)
print(f"The {n}th number in the Fibonacci sequence is {result}.")
