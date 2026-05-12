#### Q.4 : Python Program to Find the Second Largest Number in a List Using Bubble Sort.

def second_largest(numbers):

    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    print(f'Sorted List is {numbers}.')
    print("Second Largest Number =", numbers[-2])

numbers = [12, 45, 7, 89, 23]

second_largest(numbers)