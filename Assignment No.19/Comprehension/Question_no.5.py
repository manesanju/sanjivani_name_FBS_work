#### Q.5 : Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a sentence: ")

words = [word for word in text.split() if len(word) < 5]

print(words)