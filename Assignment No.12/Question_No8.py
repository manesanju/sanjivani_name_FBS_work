#### Q.8 : Python Program to Remove the Characters of Odd Index Values in a String

def remove_odd_index(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
    return result

string = input("Enter a string: ")
new_string = remove_odd_index(string)
print("String after removing odd index characters:", new_string)