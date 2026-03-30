#####Q.7 : Program to Find the Roots of a Quadratic Equation

# Take input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate discriminant
D = b*b - 4*a*c
print(D)
# Calculate roots
root1 = (-b + D**0.5) / (2*a)
root2 = (-b - D**0.5) / (2*a)

# Display result
print(f'The roots of equation are {root1} and {root2}.')