##### Q.12 : Write a program to check if given 3 digit number is a palindrome or not.

# Take input
num = int(input("Enter a 3-digit number: "))
temp = num

# Reverse number
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10

rev = d1 * 100 + d2 * 10 + d3

# Check palindrome
if temp == rev:
    print(f'{temp} is a palindrome number.')
else:
    print(f'{temp} is not a palindrome number.')