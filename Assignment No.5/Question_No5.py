##### Q.5 : Write a program to print prime numbers between 1 to 100.

# while loop
num = 2

while num <= 100:
    i = 2
    count = 0

    while i <= num:
        if num % i == 0:
            count += 1
        i += 1

    if count == 1:
        print(num, end=" ")

    num += 1

# for loop
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")