#### Q.1 : Write a Python program to find elements in a given set that are not in another set.

def difference(a, b):
    return a - b

a = {1, 2, 3, 4}
b = {3, 4, 5}

print("Elements not in second set:", difference(a, b))