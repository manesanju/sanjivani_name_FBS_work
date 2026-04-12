##### Q.6 : Write a program to print first n prime numbers.

# while loop
n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:
    i = 2
    is_prime = True

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1

# for loop
n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

for _ in range(n * 10):   # extra range to ensure enough numbers
    if count == n:
        break

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1