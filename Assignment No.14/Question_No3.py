#### Q.3 : Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def word_frequency(words):
    unique_words = set(words)

    print("Unique words:", unique_words)

    for word in unique_words:
        print(word, ":", words.count(word))

strings = ["apple", "banana", "apple", "orange", "banana", "grape"]

word_frequency(strings)