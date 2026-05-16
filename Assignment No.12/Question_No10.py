#### Q.10 : Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def string_length(text):
    count = 0
    for ch in text:
        count += 1
    return count

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
len1 = string_length(string1)
len2 = string_length(string2)
if len1 > len2:
    print("Larger string is:", string1)
elif len2 > len1:
    print("Larger string is:", string2)
else:
    print("Both strings are of equal length")