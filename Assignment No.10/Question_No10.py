#### Q.10 : Write a program to remove all occurrences of a given element in the list.

numbers = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

new_list = []

for i in numbers:
    if i != num:
        new_list += [i]

print(f'List after removal is {new_list}.')