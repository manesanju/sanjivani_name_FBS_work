##### Q.3 : WAP to print sum of series upto n

# while loop
sum = 0
num = int(input("Enter a number: "))

i = 1
while i <= num:
    sum += i
    i += 1

print(f"The sum of series is {sum}.")

# for loop
sum = 0
num = int(input('Enter a number:'))
for i in range(1, num+1):
    sum += i
print(f'The sum of series is {sum}.')