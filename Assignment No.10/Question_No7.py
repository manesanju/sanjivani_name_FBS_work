#### Q.7 : Write a program to create a new list from existing list which contains cube of each number of list.

def cubeList():

    numbers = [1, 2, 3, 4, 5]

    cube_list = []

    for i in numbers:
        cube = i * i * i
        cube_list += [cube]

    print("Cube list =", cube_list)

cubeList()