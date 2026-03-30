##### Q.9 : Write a program to swap two numbers without using third variable.

# Take input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Swapping without third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Display result
print("After swapping:")
print("First number =", num1)
print("Second number =", num2)