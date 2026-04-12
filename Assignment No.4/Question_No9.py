##### Q.9 : WAP to print all numbers in a range divisible by a given number.

# while loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
d = int(input("Enter divisor: "))

i = start
while i <= end:
    if i % d == 0:
        print(i, end=" ")
    i += 1

# for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
d = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % d == 0:
        print(i, end=" ")