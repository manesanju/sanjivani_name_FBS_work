#### Q.6 : Python Program to Multiply All the Items in a Dictionary

def multiply_dictionary_items(dictionary):
    product = 1
    for key in dictionary:
        product *= dictionary[key]
    return product

dictionary = {
    "a": 2,
    "b": 3,
    "c": 4
}

result = multiply_dictionary_items(dictionary)
print("Product of all items:", result)