#### Q.5 : Python Program to Count the Number of Vowels in a String

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

string = input("Enter a string: ")
result = count_vowels(string)
print("Number of vowels:", result)