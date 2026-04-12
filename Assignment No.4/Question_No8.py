##### Q.8 : WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# while loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

i = start
while i <= end:
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1

# for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
