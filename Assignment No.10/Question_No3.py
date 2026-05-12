#### Q.3 : Write a program to find the second largest element in the list.

def secondLargestNo():

    numbers = [12, 45, 7, 89, 23]

    largest = numbers[0]
    second_largest = numbers[0]

    for i in numbers:
        if i > largest:
            second_largest = largest
            largest = i

        elif i > second_largest and i != largest:
            second_largest = i

    print(f'Second largest element is {second_largest}.')

secondLargestNo()