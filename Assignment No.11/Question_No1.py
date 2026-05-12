#### Q.1 : Python Program to Put Even and Odd elements of a List into two Different Lists

def separate(numbers):

    even_list = []
    odd_list = []

    for i in numbers:
        if i % 2 == 0:
            even_list += [i]
        else:
            odd_list += [i]

    print(f'Even List is {even_list}.')
    print(f'Odd List is {odd_list}.')

numbers = [10, 15, 20, 25, 30, 35]

separate(numbers)