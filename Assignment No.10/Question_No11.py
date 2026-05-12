#### Q.11 : Write a program to print all numbers which are divisible by m and n in the list.

numbers = [10, 12, 15, 20, 30, 40, 60]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print(f'Numbers divisible by {m} & {n}.')

for i in numbers:
    if i % m == 0 and i % n == 0:
        print(i)