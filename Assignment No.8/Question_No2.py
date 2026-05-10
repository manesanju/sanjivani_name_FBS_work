#### Q.2 : Write a program to calculate area of circle

def area_circle(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input('Enter a radius:'))
result = area_circle(radius)
print(f'The area of circle {radius} is {result}.')