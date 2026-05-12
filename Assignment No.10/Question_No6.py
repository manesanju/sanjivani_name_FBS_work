#### Q.6 : Write a program to remove duplicates from the list.

def removeDuplicate():

    numbers = [10, 20, 30, 20, 40, 10, 50]

    new_list = []

    for i in numbers:
        if i not in new_list:
            new_list += [i]

    print(new_list)

removeDuplicate()