##### Q.6 : WAP to check if a given number is prime number or not.

# while loop
num = int(input("Enter a number: "))

count = 0
i = 1

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# for loop
num = int(input("Enter a number: "))

count = 0
i = 1

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")