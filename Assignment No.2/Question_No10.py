##### Q.10 : Write a program to reverse three-digit number.

# Take input
num = int(input("Enter a three-digit number: "))
num1 = num

# Reverse logic
d1 = num1 % 10          # last digit
num1 = num1 // 10

d2 = num1 % 10          # middle digit
num1 = num1 // 10

d3 = num1 % 10          # first digit
num1 = num1 // 10

rev = d1 * 100 + d2 * 10 + d3

# Display result
print(f'The reverse number of {num} is {rev}')