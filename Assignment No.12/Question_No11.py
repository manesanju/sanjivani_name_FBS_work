#### Q.11 : Python Program to replace every blank space with hyphen in a string.

def replace_space(text):
    result = ""
    for ch in text:
        if ch == " ":
            result += "-"
        else:
            result += ch
    return result

string = input("Enter String: ")
new_string = replace_space(string)
print("Modified string:", new_string)