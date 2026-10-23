def fibonacci(n):
    # Base cases: return 0 for the first term and 1 for the second term
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: add the two preceding terms
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Set the number of terms you want to print
terms = 10

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")