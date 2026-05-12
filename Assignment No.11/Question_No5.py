#### Q.5 : Python Program to Sort a List According to the Length of the Elements within the list.

def sort_length(words):

    for i in range(len(words)):
        for j in range(i + 1, len(words)):

            if len(words[i]) > len(words[j]):

                temp = words[i]
                words[i] = words[j]
                words[j] = temp

    print(f'Sorted List is {words}.')


# Main Program

words = ["apple", "kiwi", "banana", "grapes", "fig"]

sort_length(words)