#### Q.7 : Python Program to Find the Intersection of Two Lists.

def intersection_list(list1, list2):

    intersection = []

    for i in list1:

        if i in list2 and i not in intersection:
            intersection += [i]

    print("Intersection of Lists =", intersection)


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

intersection_list(list1, list2)