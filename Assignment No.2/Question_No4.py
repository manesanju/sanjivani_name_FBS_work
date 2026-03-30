##### Q.4 : WAP to calculate area of triangle and rectangle

# Triangle Area
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

triangle_area = 0.5 * base * height

# Rectangle Area
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

rectangle_area = length * breadth

# Display result
print(f'Area of triangle is {triangle_area}')
print(f'Area of rectangle is {rectangle_area}')