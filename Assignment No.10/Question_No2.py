#### Q.2 : Write a program to find maximum and minimum element in a list.

def maxMinNo():
    
    numbers = [12, 45, 7, 89, 23]

    maximum = numbers[0]
    minimum = numbers[0]

    for i in numbers:
        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    print(f'Maximum element is {maximum}.')
    print(f'Minimum element is {minimum}.')

maxMinNo()