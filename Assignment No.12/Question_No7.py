#### Q.7 : Python Program to Calculate the Length of a String Without Using a Library Function

def string_length(text):
    count = 0
    for ch in text:
        count += 1
    return count

string = input("Enter a string: ")
length = string_length(string)
print("Length of the string is:", length)