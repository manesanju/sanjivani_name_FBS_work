##### Q.7 : Find the sum of three-digit number.

# Take input
num = int(input("Enter a three-digit number: "))

# Extract digits
d1 = num % 10          # last digit
num = num // 10

d2 = num % 10          # middle digit
num = num // 10

d3 = num % 10          # first digit

# Calculate sum
sum_digits = d1 + d2 + d3

# Display result
print(f'Sum of {d1} + {d2} + {d3} is {sum_digits}')