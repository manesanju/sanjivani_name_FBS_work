#### Q.1 : Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_character(text):
    result = ""

    for ch in text:
        if ch == 'a':
            result += '$'
        else:
            result += ch
    return result

string = input("Enter a string: ")
new_string = replace_character(string)
print("Modified string:", new_string)