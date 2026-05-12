#### Q.8 : Write a program to create a duplicate of an existing list. It should not point to same list.

list1 = [10, 20, 30, 40, 50]

list2 = []

for i in list1:
    list2 += [i]

print("Original List =", list1)
print("Duplicate List =", list2)