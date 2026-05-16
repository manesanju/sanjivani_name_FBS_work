#### Q.12 : Python Program to count number of lowercase characters in a string.

def count_lowercase(text):
    count = 0
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            count += 1
    return count

string = input("Enter a string: ")
result = count_lowercase(string)
print("Number of lowercase characters:", result)