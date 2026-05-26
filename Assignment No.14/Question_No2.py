#### Q.2 : Write a Python program to remove the intersection of a second set with a first set.

def remove_intersection(a, b):
    return a - b

a = {1, 2, 3, 4}
b = {3, 4, 5}

print("After removing intersection:", remove_intersection(a, b))