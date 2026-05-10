#### Q.2 : Write a program to check if given number is Armstrong or not using recursive function.

# Recursive function to find Armstrong sum
def armstrong(n, power):
    if n == 0:
        return 0
    
    digit = n % 10
    return (digit ** power) + armstrong(n // 10, power)

num = int(input("Enter a number: "))

# Count number of digits
power = len(str(num))

# Find Armstrong sum
result = armstrong(num, power)

# Check Armstrong number
if result == num:
    print(f'The {num} is an Armstrong number.')
else:
    print(f'The {num} is not an Armstrong number.')