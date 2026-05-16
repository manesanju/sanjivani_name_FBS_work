#### Q.7 : Python Program to Remove the Given Key from a Dictionary

def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print("Key removed successfully")
    else:
        print("Key not found")

dictionary = {
    "name": "Sanjivani",
    "age": 20,
    "city": "Pune"
}

key = input("Enter the key to remove: ")
remove_key(dictionary, key)
print("Updated Dictionary:", dictionary)