#### Q.13 : Python Program to count number of digits and letters in a string.

def count_digits_letters(text):
    digits = 0
    letters = 0

    for ch in text:
        if ch >= '0' and ch <= '9':
            digits += 1
        elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            letters += 1
    return digits, letters

string = input("Enter a string: ")
digit_count, letter_count = count_digits_letters(string)
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)