##### Q.10 : WAP to check if given number is Perfect Number.

# while loop
num = int(input("Enter a number: "))

sum = 0
i = 1

while i < num:
    if num % i == 0:
        sum += i
    i += 1

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# for loop
num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
