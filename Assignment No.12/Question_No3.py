#### Q.3 : Python Program to Detect if Two Strings are Anagrams

def check_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if check_anagram(string1, string2):
    print("The strings are Anagrams")
else:
    print("The strings are Not Anagrams")