#####Q.6 : Write a Program to input two angles from user and find third angle of the triangle.

# Take input for two angles
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))

# Calculate third angle
angle3 = 180 - (angle1 + angle2)

# Display result
print(f'The third angle of triangle with angles {angle1} & {angle2} is {angle3}.')