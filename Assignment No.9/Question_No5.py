#### Q.5 : Write a program to find factorial using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
result = factorial(n)
print(f'The factorial of {n} is {result}.')