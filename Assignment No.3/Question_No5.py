##### Q.5 : Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# Take input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check triangle type
if a == b and b == c:
    print(f'The side of {a} & {b} & {c} is a Equilateral Triangle.')
elif a == b or b == c or a == c:
    print(f'The side of {a} & {b} & {c} is aIsosceles Triangle.')
else:
    print(f'The side of {a} & {b} & {c} is aScalene Triangle.')