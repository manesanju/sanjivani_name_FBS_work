##### Q.4 : Write a program to input all sides of a triangle and check whether triangle is valid or not.

# Take input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check conditions 
if a + b > c:
    if a + c > b:
        if b + c > a:
            print(f"The sides {a}, {b}, {c} is a valid triangle.")
        else:
            print(f"The sides {a}, {b}, {c} is not a valid triangle.")
    else:
        print(f"The sides {a}, {b}, {c} is not a valid triangle.")
else:
    print(f"The sides {a}, {b}, {c} is not a valid triangle.")