#### Q.4 : Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def find_pairs(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                print(lst[i], lst[j])

numbers = [1, 2, 3, 4, 5, 6]
target = 7

find_pairs(numbers, target)