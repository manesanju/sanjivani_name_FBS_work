#### Q.4 : Write a program to reverse the list.

def reverse():

    numbers = [10, 20, 30, 40, 50]

    start = 0
    end = len(numbers) - 1

    while start < end:
        temp = numbers[start]
        numbers[start] = numbers[end]
        numbers[end] = temp

        start = start + 1
        end = end - 1

    print(f'Reversed list is {numbers}.')

reverse()