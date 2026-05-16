#### Q.2 : Python Program to Remove the nth Index Character from a Non-Empty String

def remove_character(text, n):
    result = ""

    for i in range(len(text)):
        if i != n:
            result += text[i]
    return result

string = input("Enter a string: ")
index = int(input("Enter the index to remove: "))
new_string = remove_character(string, index)
print("Modified string:", new_string)