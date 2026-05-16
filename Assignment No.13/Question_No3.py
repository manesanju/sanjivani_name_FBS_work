#### Q.3 : Python Program to Check if a Given Key Exists in a Dictionary or Not

dictionary = {
    "name": "Sanjivani",
    "age": 20,
    "city": "Pune"
}

key = input("Enter the key to check: ")
if key in dictionary:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")