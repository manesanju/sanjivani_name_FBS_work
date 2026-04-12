##### Q.11 : WAP to check if given number Strong Number.

# while loop
num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1

    sum += fact
    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")

# for loop
num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")