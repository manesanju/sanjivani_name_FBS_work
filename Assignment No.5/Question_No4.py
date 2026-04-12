##### Q.4 : WAP to print Armstrong number within a given range

# while loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

num = start

while num <= end:
    sum = 0
    digits = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num, end=" ")

    num += 1

# for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    sum = 0
    digits = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num, end=" ")