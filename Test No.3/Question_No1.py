# Q.1: Write a program to print first n prime numbers

n = int(input('Enter number: '))

num = 2
count = 0

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1

    num += 1