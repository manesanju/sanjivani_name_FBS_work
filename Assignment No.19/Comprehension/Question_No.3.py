#### Q.3 : Count the number of spaces in a string (take input from user)

text = input("Enter a string: ")

spaces = len([ch for ch in text if ch == ' '])

print("Number of spaces =", spaces)