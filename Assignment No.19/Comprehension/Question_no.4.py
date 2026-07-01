#### Q.4 : Remove all of the vowels in a string (take input from user)

text = input("Enter a string: ")

result = ''.join([ch for ch in text if ch.lower() not in 'aeiou'])

print("String after removing vowels:")
print(result)