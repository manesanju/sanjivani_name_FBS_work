##### Q.3 : Write a program to input angles of a triangle and check whether triangle is valid or not.

# Take input
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

# Check condition
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print(f'The angles of {a} & {b} & {c} is a valid triangle')
else:
    print(f'The angles of {a} & {b} & {c} is not a valid triangle')