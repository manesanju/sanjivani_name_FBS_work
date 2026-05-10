#### Q.5 : Sum of all prime numbers between 1 to n

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def sum_prime(n):
    total = 0
    for i in range(1, n + 1):
        if is_prime(i):
            total = total + i

    return total

n = int(input('Enter value of n: '))
result = sum_prime(n)
print(f'The sum of prime numbers of {n} is {result}.')