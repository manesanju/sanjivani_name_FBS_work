#### Q.3 : Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
        
    return total

n = int(input('Enter value of n: '))

print(f'The sum of series {n} is {sum_series(n)}.')


# b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
        
    return fact

def sum_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + factorial(i)
        
    return total

n = int(input('Enter value of n: '))
print(f' The sum of factorial series of {n} is {sum_factorial_series(n)}.')


# c. 1^1 + 2^2 + 3^3+ ...... n^n

def power_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
        
    return total

n = int(input('Enter value of n: '))
print(f'The sum of power series of {n} is {power_series(n)}.')