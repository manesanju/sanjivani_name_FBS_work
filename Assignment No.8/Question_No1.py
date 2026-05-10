#### Q.1 : Write a program to calculate area of rectangle

def area_rectangle(length, width):
    area = length * width
    return area

length = float(input('Enter length: '))
width = float(input('Enter width: '))
result = area_rectangle(length, width)
print(f' The area of rectangle length {length} and width {width} is: {result}.')