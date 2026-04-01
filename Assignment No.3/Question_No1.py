##### Q.1 : Write a program to check if the given number is positive or negative.

# Take input
num = int(input("Enter a number: "))

# Check condition
if(num == 0):
    print('The number is neutral')
elif(num > 0):
    print(f'{num} is a positive number')
else:
    print(f'{num} is a negative number')