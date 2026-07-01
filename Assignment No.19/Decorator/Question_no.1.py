#### Q.1 : Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

# Memoization Decorator

def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            print("Returning Cached Value...")
            return cache[n]
        else:
            result = func(n)
            cache[n] = result
            return result

    return wrapper


# Recursive Fibonacci Function
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Main Program
num = int(input("Enter a number: "))

print("Fibonacci Number =", fibonacci(num))

# Calling again to show cached result
print("Fibonacci Number =", fibonacci(num))