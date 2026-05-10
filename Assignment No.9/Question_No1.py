#### Q.1 : Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

# Recursive function to find factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# Recursive function to find sum of series
def series_sum(n):
    if n == 1:
        return 1
    return fact(n) + series_sum(n - 1)

n = int(input('Enter value of n: '))
print(f'The sum of series of {n} is {series_sum(n)}.')