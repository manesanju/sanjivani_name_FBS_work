#### Q.7 : Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def find_missing(set1, set2):
    print("Missing in second set:", set1 - set2)
    print("Missing in first set:", set2 - set1)

a = {1, 2, 3, 4, 5}
b = {2, 4, 6}

find_missing(a, b)