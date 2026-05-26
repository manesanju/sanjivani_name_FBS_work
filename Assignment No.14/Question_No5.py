#### Q.5 : Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_prefix(strings):
    prefix = ""

    for i in range(len(strings[0])):
        chars = set()

        for word in strings:
            if i >= len(word):
                return prefix
            chars.add(word[i])

        if len(chars) == 1:
            prefix += strings[0][i]
        else:
            break

    return prefix

words = ["flower", "flow", "flight"]

print("Longest Common Prefix:", longest_prefix(words))