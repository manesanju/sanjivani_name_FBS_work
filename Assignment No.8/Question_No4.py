#### Q.4 : Sum of all odd numbers between 1 to n

def sum_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total = total + i

    return total

n = int(input('Enter value of n: '))
result = sum_odd(n)
print(f'The sum of odd numbers of {n} is {result}.')