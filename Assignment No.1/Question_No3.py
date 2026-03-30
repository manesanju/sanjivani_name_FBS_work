##### Q.3 : Program to find quotient and remainder of two numbers.

# To take dividend and divisor
dividend = int(input('Enter the dividend number:'))
divisor = int(input('Enter the divisor number:'))

# Find Quetient
Quetient = dividend // divisor

# Find Remainder
Remainder = dividend % divisor

# Display Result
print(f'The Quetient of {dividend} & {divisor} is {Quetient}.')
print(f'The Remainder of {dividend} & {divisor} is {Remainder}.')