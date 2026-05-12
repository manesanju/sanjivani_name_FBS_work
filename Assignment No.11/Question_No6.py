#### Q.6 : Python Program to Find the Union of two Lists.

def union_list(list1, list2):

    union = []

    for i in list1:
        if i not in union:
            union += [i]

    for i in list2:
        if i not in union:
            union += [i]

    print(f'Union of Lists is {union}.')

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

union_list(list1, list2)