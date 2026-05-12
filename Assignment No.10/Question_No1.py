#### Q.1 : Write a program to find sum of all elements of list

def sum():
    
    numbers = [10, 20, 30, 40, 50]

    total = 0

    for i in numbers:
        total = total + i

    print(f'Sum of all elements is {total}.')

sum()