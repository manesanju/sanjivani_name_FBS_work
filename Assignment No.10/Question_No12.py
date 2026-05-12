#### Q.12 : Write a program to create three lists of numbers, their squares and cubes.

def cubeSquare():
    numbers = [1, 2, 3, 4, 5]

    square_list = []
    cube_list = []

    for i in numbers:
        square_list += [i * i]
        cube_list += [i * i * i]

    print(f'Numbers List is {numbers}.')
    print(f'Squares List is {square_list}.')
    print(f'Cubes List is {cube_list}.')

cubeSquare()