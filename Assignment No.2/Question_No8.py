##### Q.8 : Write a program to swap two numbers using third variable.

# Take input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Swapping using third variable
temp = num1
num1 = num2
num2 = temp

# Display result
print("After swapping:")
print("First number =", num1)
print("Second number =", num2)