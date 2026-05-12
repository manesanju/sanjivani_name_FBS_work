#### Q.10 : Write a program to print list after removing even numbers.

def remove_even(lst):
    odd_list = []
    i = 0
    j = 0

    while i < len(lst):
        if lst[i] % 2 != 0:
            odd_list = odd_list + [lst[i]]
        i = i + 1

    print(f'List after removing even numbers is {odd_list}.')

numbers = [10, 15, 20, 25, 30, 35, 40, 45]
remove_even(numbers)