#### Q.14 : Python Program to count the occurrences of ach word in a string.

def count_word_occurrences(text):
    words = text.split()
    counted = []

    for word in words:
        if word not in counted:
            count = 0

            for w in words:
                if word == w:
                    count += 1

            print(word, ":", count)
            counted.append(word)

string = input("Enter a string: ")
count_word_occurrences(string)