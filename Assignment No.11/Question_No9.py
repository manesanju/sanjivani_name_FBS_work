#### Q.9 : Write a program to create three lists of numbers, their squares and cubes.

def create_lists(n):
    numbers = [0] * n
    squares = [0] * n
    cubes = [0] * n

    i = 0
    while i < n:
        numbers[i] = i + 1
        squares[i] = (i + 1) * (i + 1)
        cubes[i] = (i + 1) * (i + 1) * (i + 1)
        i = i + 1

    print("Numbers List :", numbers)
    print("Squares List :", squares)
    print("Cubes List   :", cubes)

n = int(input("Enter the limit: "))
create_lists(n)