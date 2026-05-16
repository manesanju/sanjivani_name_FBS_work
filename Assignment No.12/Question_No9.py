#### Q.9 : Python Program to Calculate the Number of Words and the Number of Characters Present in a String

def count_words_characters(text):
    word_count = 0
    char_count = 0

    for ch in text:
        char_count += 1

    words = text.split()

    for word in words:
        word_count += 1

    return word_count, char_count

string = input("Enter a string: ")
words, characters = count_words_characters(string)
print("Number of words:", words)
print("Number of characters:", characters)