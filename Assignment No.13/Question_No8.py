#### Q.8 : Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


string = input("Enter a string: ")
result = word_frequency(string)
print("Word Frequencies:")
for key in result:
    print(key, ":", result[key])