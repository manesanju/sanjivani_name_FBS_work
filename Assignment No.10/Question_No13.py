#### Q.13 : Write a program to print list after removing even numbers.

def oddNo():
    numbers = [10, 15, 20, 25, 30, 35]

    new_list = []

    for i in numbers:
        if i % 2 != 0:
            new_list += [i]

    print(f'List after removing even numbers is {new_list}.')

oddNo()