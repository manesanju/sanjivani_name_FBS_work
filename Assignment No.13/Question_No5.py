#### Q.5 : Python Program to Sum All the Items in a Dictionary

def sum_dictionary_items(dictionary):
    total = 0
    for key in dictionary:
        total += dictionary[key]
    return total

dictionary = {
    "a": 10,
    "b": 20,
    "c": 30
}
result = sum_dictionary_items(dictionary)
print("Sum of all items:", result)