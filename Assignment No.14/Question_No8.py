#### Q.8 : Write a Python program to find all the anagrams and group them together from a given list of strings.

def group_anagrams(words):
    anagrams = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    for group in anagrams.values():
        print(group)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

group_anagrams(words)