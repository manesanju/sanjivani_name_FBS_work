#### Q.6 : Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replace_space(text):
    result = ""
    for ch in text:
        if ch == " ":
            result += "-"
        else:
            result += ch
    return result

string = input("Enter a string: ")
new_string = replace_space(string)
print("Modified string:", new_string)