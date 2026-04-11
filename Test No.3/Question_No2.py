# Q.2: Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input('Enter number: '))

fact = 1
total = 0

for i in range(1, n + 1):
    fact = fact * i      # calculate factorial step by step
    total = total + (i / fact)

print(f'The sum of series {n} is {total}.')